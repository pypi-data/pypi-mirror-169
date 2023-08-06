"""
Two classes:
  - RealmAuthenticator
  - OIDCClientAuthenticator

Dependencies:
  - PyJWT: API to decode JWT tokens
  - cryptography: Cryptography algorithms
  - pydantic: JSON validation library
  - httpx: Async HTTP client

Default well-known: https://lemur-16.cloud-iam.com/auth/realms/quara-demo/.well-known/openid-configuration

Allowed Grant types:
  - authorization_code
  - refresh_token
  - password
  - client_credentials

Additional helper:
  - Browser login
  - Decode token
  - Decode access token
  - Decode ID token
"""
import asyncio
import contextlib
import os
import time
import types
import typing as t
import urllib.parse
import warnings

import httpx
import jwt
import jwt.algorithms
import jwt.exceptions
from pydantic import BaseModel, Extra, Field
from pydantic.validators import bool_validator

ScopeType = t.Union[str, t.List[str], t.Tuple[str], t.Set[str]]

DEFAULT_WELL_KNOWN = "https://lemur-16.cloud-iam.com/auth/realms/quara-demo/.well-known/openid-configuration"
DEFAULT_SCOPES: t.List[str] = []


class UnauthorizedError(Exception):
    """Common class for exceptions related to authentication and authorization"""

    pass


class PendingCredentials:
    """A wrapper around asyncio.Future
    because future do not play nice with pydantic."""

    def __init__(self) -> None:
        self.future: "asyncio.Future[Credentials]" = asyncio.Future()


class PendingDeviceAuthorization(
    BaseModel, extra=Extra.allow, arbitrary_types_allowed=True
):
    """All data related to a pending device authorization."""

    device_code: str
    user_code: str
    verification_uri: str
    verification_uri_complete: str
    expires_in: int
    interval: float
    pending: PendingCredentials

    async def wait_for_credentials(self) -> "Credentials":
        """Wait until credentials are returned.

        Raises asyncio.CancelledError if request has been cancelled.
        Raises the exception encountered during request if request failed.
        """
        return await self.pending.future

    def get_credentials(self) -> "Credentials":
        """Get credentials.

        Raises asyncio.InvalidStateError if request is still pending.
        Raises asyncio.CancelledError if request has been cancelled.
        Raises the exception encountered during request if request failed.
        """
        return self.pending.future.result()

    def set_credentials(self, value: "Credentials") -> None:
        """Set the credentials once device authorization grant succeeded.
        This method is reserved for internal usage."""
        self.pending.future.set_result(value)

    def set_exception(self, exception: BaseException) -> None:
        """Set the credentials once device authorization grant succeeded.
        This method is reserved for internal usage."""
        self.pending.future.set_exception(exception)


class RawCredentials(BaseModel, extra=Extra.allow):
    """JSON data received from OIDC token endpoint"""

    access_token: str
    id_token: t.Optional[str] = None
    refresh_token: t.Optional[str] = None


class BaseJWT(BaseModel, extra=Extra.allow, allow_population_by_field_name=True):
    """Common fields between OIDC ID Token and OAuth2 Access Token.
    Additional fields will also be accepted but will not be validated.

    Should work both with Keycloak and Azure AD.

    Microsoft docs: https://learn.microsoft.com/en-us/azure/active-directory/develop/access-tokens
    """

    # Indicate type of the token
    typ: str
    # Identifies the intended audience of the token
    aud: str
    # Issuing authority
    iss: str
    # Specifies when the authentication for this token occurred
    iat: int
    # Represents the tenant that the user is signing in to
    sub: str
    # Specifies the expiration time on or after which the JWT must not be accepted for processing
    exp: int
    # Token identifier claim
    jti: str = Field(alias="uti")
    # The primary username that represents the user. The value could be an email address, phone number, or a generic username without a specified format.
    preferred_username: str
    # Optional additional user infos (Keycloak fields)
    email: t.Optional[str] = None
    email_verified: t.Optional[bool] = None
    family_name: t.Optional[str] = None
    given_name: t.Optional[str] = None
    name: t.Optional[str] = None
    # Optional additional sessions infos (Keycloak fields)
    session_state: t.Optional[str] = None
    sid: t.Optional[str] = None
    # Optional azure fields
    idp: t.Optional[str] = None
    oid: t.Optional[str] = None
    tid: t.Optional[str] = None


class Access(BaseModel, extra=Extra.allow):
    """Access holds a list of roles"""

    roles: t.List[str] = []


class AccessToken(BaseJWT, allow_population_by_field_name=True):
    """Access token received from OIDC provider."""

    scope: str = Field(alias="scp")
    # A value of 0 for the "Authentication context class" claim indicates
    # that the end-user authentication didn't meet the requirements of ISO/IEC 29115.
    acr: str
    # The client ID for which token was emitted
    azp: str
    # Additional keycloack fields
    realm_access: t.Optional[Access] = None
    resource_access: t.Optional[t.Dict[str, Access]] = None
    allowed_origins: t.Optional[t.List[str]] = Field(None, alias="allowed-origins")
    # Optional additional Azure fields
    roles: t.Optional[t.List[str]] = None
    groups: t.Optional[t.List[str]] = None
    hasGroups: t.Optional[t.Literal[True]] = None
    wids: t.Optional[t.List[str]] = None


class IDToken(BaseJWT):
    """ID token received from OIDC provider."""

    at_hash: str
    auth_time: int


class Credentials(BaseModel, extra=Extra.ignore):
    """Validated access token and optionally id token."""

    access_token: AccessToken
    id_token: t.Optional[IDToken] = None
    raw: RawCredentials


class RequestProtocol(t.Protocol):
    """Request must expose a cookies attribute and a headers attribute."""

    cookies: t.Mapping[str, str]
    headers: t.Mapping[str, str]


def write_scope(
    scope: t.Optional[ScopeType], default_scopes: t.Iterable[str] = DEFAULT_SCOPES
) -> str:
    """Write scopes as a space-delimited string."""
    if isinstance(scope, str):
        target_scopes = scope.split(" ")
    elif scope is None:
        target_scopes = []
    else:
        target_scopes = list(scope)
    if default_scopes:
        target_scopes.extend(
            [scope for scope in default_scopes if scope not in target_scopes]
        )
    return " ".join(target_scopes).strip()


def read_scope(scope: t.Optional[ScopeType]) -> t.List[str]:
    if scope is None:
        return []
    if isinstance(scope, str):
        return scope.split(" ")
    return list(set(scope))


async def http_client_factory() -> httpx.AsyncClient:
    return httpx.AsyncClient()


class RealmAuthenticator:
    """An RealmAuthenticator communicates with an OIDC provider to perform one of the
    following grants:
        - Password grant
        - Client credentials grant
        - Authorization code grant
        - Refresh grant
    """

    def __init__(
        self,
        well_known_uri: str = DEFAULT_WELL_KNOWN,
        default_scopes: t.Optional[ScopeType] = None,
        httpx_factory: t.Callable[
            [], t.Coroutine[None, None, httpx.AsyncClient]
        ] = http_client_factory,
    ) -> None:
        """Create a new RealmAuthenticator instance.

        Arguments:
            well_known_uri: An URL pointing to well known OIDC configuration.
        """
        self.http: t.Optional[httpx.AsyncClient] = None
        self._http_factory = httpx_factory
        self.default_algorithms = jwt.algorithms.get_default_algorithms()
        self.default_scopes = read_scope(default_scopes or DEFAULT_SCOPES)
        self.well_known_uri = well_known_uri
        self.well_known: t.Dict[str, t.Any] = {}
        self._issuer_public_key: t.Optional[t.Any] = None
        self._issuer_public_jwk: t.Optional[t.Dict[str, t.Any]] = None
        self._algorithm: t.Optional[str] = None

    async def __aenter__(self) -> "RealmAuthenticator":
        await self.start()
        return self

    async def __aexit__(
        self,
        exc_type: t.Optional[BaseException] = None,
        exc: t.Optional[BaseException] = None,
        tb: t.Optional[types.TracebackType] = None,
    ) -> None:
        await self.stop()
        return None

    async def start(self) -> None:
        """Start the authenticator."""
        if self.http is None:
            self.http = await self._http_factory()
        well_known = await self.http.get(self.well_known_uri)
        well_known.raise_for_status()
        self.well_known.update(well_known.json())
        await self.fetch_issuer_public_key()

    async def stop(self) -> None:
        """Stop the authenticator."""
        if self.http:
            await self.http.aclose()
            self.http = None

    def get_url(self, endpoint: str) -> str:
        """Get the URl for given endpoint.

        Arguments:
            endpoint: a valid endpoint name from the OpenID Connect Discovery 1.0 specification

        Examples:
            >>> async with RealmAuthenticator() as auth:
            >>>     auth_url = auth.get_url("authorization_endpoint")
            >>>     token_url = auth.get_url("token_endpoint")
        """
        try:
            return str(self.well_known[endpoint])
        except KeyError:
            raise KeyError(
                f"No URL configured for endpoint: {endpoint}. Make sure authenticator is started."
            )

    def get_authorization_url(
        self,
        client_id: str,
        redirect_uri: str,
        scope: t.Optional[ScopeType] = None,
        state: t.Optional[str] = None,
        response_type: str = "code",
    ) -> str:
        """
        Get authorization URL to redirect the resource owner to.
        https://tools.ietf.org/html/rfc6749#section-4.1.1

        Arguments:
            client_id: OIDC client ID
            redirect_uri: Absolute URL of the client where the user-agent will be redirected to.
            scope: Space delimited list of strings, or iterable of strings.
            state: An opaque value used by the client to maintain state between the request and callback.
            response_type: Use "code" to perform authorization grant, or "token" to perform implicit grant.

        Return:
            URL to redirect the resource owner to.
        """
        optional_parameters: t.Dict[str, t.Any] = {}
        if state:
            optional_parameters["state"] = state
        params = urllib.parse.urlencode(
            {
                "client_id": client_id,
                "response_type": response_type,
                "redirect_uri": redirect_uri,
                "scope": write_scope(scope, self.default_scopes),
                **optional_parameters,
            }
        )
        url = self.get_url("authorization_endpoint")
        return "{}?{}".format(url, params)

    def get_public_client(
        self,
        client_id: str,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> "PublicClientAuthenticator":
        """Get an authenticator for a single OIDC public client within the authenticator realm."""
        return PublicClientAuthenticator(
            self,
            client_id=client_id,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
        )

    def get_confidential_client(
        self,
        client_id: str,
        client_secret: str,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> "ConfidentialClientAuthenticator":
        """Get an authenticator for a single OIDC condifdential client within the authenticator realm."""
        return ConfidentialClientAuthenticator(
            self,
            client_id=client_id,
            client_secret=client_secret,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
        )

    def get_algorithm(self) -> str:
        """Get algorithm used to validate JWT"""
        if self._algorithm:
            return self._algorithm
        raise ValueError(
            "Algorithm is not configured. Make sure authenticator is started."
        )

    def get_issuer_public_key(self) -> t.Any:
        """Get public key used to validate JWT."""
        if self._issuer_public_key:
            return self._issuer_public_key
        raise ValueError(
            "Issuer public key is not configured. Make sure authenticator is started."
        )

    def get_issuer_public_jwk(self) -> t.Dict[str, t.Any]:
        """Get public jwk used to validate user JWT"""
        if self._issuer_public_jwk:
            return self._issuer_public_jwk
        raise ValueError(
            "Issuer public key is not configured. Make sure authenticator is started."
        )

    def decode_token(
        self,
        token: str,
        audience: t.Optional[str] = None,
        verify_signature: bool = True,
        verify_audience: bool = True,
    ) -> t.Dict[str, t.Any]:
        """Decode a JWT using issuer public key.

        By default JWT signature is verified and audience is verified.

        Arguments:
            token: The token to decode as a string.
            audience: Value to check for audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            A dictionary holding fields found within JWT.
        """
        key = self.get_issuer_public_key()
        algorithm = self.get_algorithm()
        options: t.Dict[str, t.Any] = {"verify_signature": verify_signature}
        if verify_audience:
            options["verify_aud"] = True
        else:
            options["verify_aud"] = False
        if token.startswith("Bearer "):
            token = token[len("Bearer ") :]
        return jwt.decode(
            token,
            key=key,
            algorithms=[algorithm],
            audience=audience,
            options=options,
        )

    def decode_access_token(
        self,
        token: str,
        audience: t.Optional[str] = None,
        verify_signature: bool = True,
        verify_audience: bool = True,
    ) -> AccessToken:
        """Decode an OIDC access token using issuer public key.

        Access token hold informations regarding user identity, just like ID tokens,
        but they also hold authorization information such as:
          - realm access (roles)
          - resource access (roles)
          - scopes

        Arguments:
            token: The token to decode as a string.
            audience: Value to check for audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            An AccessToken instance.
        """
        return AccessToken.parse_obj(
            self.decode_token(
                token,
                audience=audience,
                verify_signature=verify_signature,
                verify_audience=verify_audience,
            )
        )

    def decode_id_token(
        self,
        token: str,
        audience: t.Optional[str] = None,
        verify_signature: bool = True,
        verify_audience: bool = True,
    ) -> IDToken:
        """Decode an OIDC ID token using issuer public key.

        ID tokens can be used to prove that user is AUTHENTICATED.
        It holds information regarding IDENTITY of the user.
        They should never be used for authorization purpose.
        Use the access token instead.

        Arguments:
            token: The token to decode as a string.
            audience: Value to check for audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            An IDToken instance.
        """
        return IDToken.parse_obj(
            self.decode_token(
                token,
                audience=audience,
                verify_signature=verify_signature,
                verify_audience=verify_audience,
            )
        )

    def decode_token_from_request(self, request: RequestProtocol) -> Credentials:
        key = "Authorization"
        if key in request.cookies:
            token = request.cookies[key]
        elif key in request.headers:
            token = request.cookies[key]
        else:
            raise ValueError("Missing authorization")
        if not token.startswith("Bearer "):
            raise ValueError("Unsupported authorization")
        access_token = self.decode_access_token(token)
        return Credentials(
            access_token=access_token, raw=RawCredentials(access_token=token)
        )

    async def _request(
        self,
        method: str,
        endpoint: str,
        *,
        bearer: t.Optional[str] = None,
        **kwargs: t.Any,
    ) -> httpx.Response:
        if self.http is None:
            raise ValueError(
                "HTTP client is not configured. Make sure authenticator is started."
            )
        url = self.get_url(endpoint)
        if bearer:
            if "headers" in kwargs:
                kwargs["headers"]["Authorization"] = f"Bearer: {bearer}"
            else:
                kwargs["headers"] = {"Authorization": f"Bearer: {bearer}"}
        response = await self.http.request(method, url, **kwargs)
        response.raise_for_status()
        return response

    async def fetch_issuer_public_key(self) -> None:
        """Fetch the issuer public key from remote OIDC provider."""
        response = await self._request("GET", "jwks_uri")
        jwks: t.List[t.Dict[str, t.Any]] = response.json()["keys"]
        for key in jwks:
            if "alg" not in key:
                alg = "RS256"
            else:
                alg = key["alg"]
            if alg in self.default_algorithms:
                self._algorithm = alg
                self._issuer_public_jwk = key
                self._issuer_public_key = self.default_algorithms[
                    self._algorithm
                ].from_jwk(key)
                break

        else:
            raise KeyError(
                f"No public found with supported algorithm ({list(self.default_algorithms)})"
            )

    async def fetch_token(
        self,
        client_id: str,
        grant_type: str,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
        **kwargs: t.Any,
    ) -> Credentials:
        """Send a request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        Arguments:
            client_id: OIDC client ID.
            grant_type: One of "authorization_code", "refresh_token", "password", "client_credentials".
            scope: Space delimited list of strings, or iterable of strings.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.
            kwargs: Extra arguments specific to each grant type.

        Returns:
            A Grant instance holding access token.
        """
        scope = write_scope(scope, self.default_scopes)
        response = await self._request(
            "POST",
            "token_endpoint",
            data={
                "client_id": client_id,
                "grant_type": grant_type,
                "scope": scope,
                **kwargs,
            },
        )
        raw = RawCredentials.parse_obj(response.json())
        return Credentials(
            access_token=self.decode_access_token(
                raw.access_token,
                audience=access_token_audience,
                verify_audience=verify_audience,
                verify_signature=verify_signature,
            ),
            id_token=self.decode_id_token(
                raw.id_token,
                audience=id_token_audience,
                verify_audience=verify_audience,
                verify_signature=verify_signature,
            )
            if raw.id_token
            else None,
            raw=raw,
        )

    async def fetch_user_infos(
        self, access_token: t.Union[str, Credentials]
    ) -> t.Dict[str, t.Any]:
        if isinstance(access_token, Credentials):
            access_token = access_token.raw.access_token
        response = await self._request(
            "GET",
            "userinfo_endpoint",
            bearer=access_token,
        )
        return response.json()  # type: ignore[no-any-return]

    async def introspect_token(
        self,
        client_id: str,
        access_token: t.Union[str, Credentials],
        client_secret: t.Optional[str] = None,
    ) -> t.Dict[str, t.Any]:
        if isinstance(access_token, Credentials):
            access_token = access_token.raw.access_token
        payload = {
            "token": access_token,
            "client_id": client_id,
        }
        if client_secret:
            payload["client_secret"] = client_secret
        response = await self._request(
            "POST",
            "introspection_endpoint",
            data=payload,
            bearer=access_token,
        )
        return response.json()  # type: ignore[no-any-return]

    async def revoke_access_token(
        self,
        client_id: str,
        access_token: t.Union[str, Credentials],
        client_secret: t.Optional[str] = None,
    ) -> None:
        if isinstance(access_token, Credentials):
            access_token = access_token.raw.access_token
        payload = {
            "client_id": client_id,
            "token": access_token,
            "token_type_hint": "access_token",
        }
        if client_secret:
            payload["client_secret"] = client_secret
        await self._request(
            "POST",
            "revocation_endpoint",
            data=payload,
            bearer=access_token,
        )

    async def revoke_refresh_token(
        self,
        client_id: str,
        refresh_token: t.Union[str, Credentials],
        access_token: t.Union[None, str, Credentials] = None,
        client_secret: t.Optional[str] = None,
    ) -> None:
        if isinstance(refresh_token, Credentials):
            token = refresh_token.raw.refresh_token
            if token is None:
                raise ValueError("refresh_token cannot be None")
            if access_token is None:
                access_token = refresh_token.raw.access_token
        if access_token is None:
            raise ValueError("bearer cannot be None")
        if isinstance(access_token, Credentials):
            access_token = access_token.raw.access_token
        payload = {
            "client_id": client_id,
            "token": token,
            "token_type_hint": "refresh_token",
        }
        if client_secret:
            payload["client_secret"] = client_secret
        await self._request(
            "POST",
            "revocation_endpoint",
            data=payload,
            bearer=access_token,
        )

    async def revoke_session(
        self,
        client_id: str,
        refresh_token: t.Union[str, Credentials],
        access_token: t.Union[None, str, Credentials] = None,
        client_secret: t.Optional[str] = None,
    ) -> None:
        """End session on OIDC provider side.

        Warning:
            This does not revoke access token associated with refresh token!
        """
        if isinstance(refresh_token, Credentials):
            token = refresh_token.raw.refresh_token
            if token is None:
                raise ValueError("refresh_token cannot be None")
            if access_token is None:
                access_token = refresh_token.raw.access_token
        if access_token is None:
            raise ValueError("bearer cannot be None")
        if isinstance(access_token, Credentials):
            access_token = access_token.raw.access_token
        payload = {
            "client_id": client_id,
            "refresh_token": token,
        }
        if client_secret:
            payload["client_secret"] = client_secret
        await self._request(
            "POST",
            "end_session_endpoint",
            data=payload,
            bearer=access_token,
        )

    async def oidc_password_grant(
        self,
        client_id: str,
        username: str,
        password: str,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> Credentials:
        """Send a password grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        Arguments:
            client_id: OIDC client ID.
            username: Name of user.
            password: Password of user.
            scope: Space delimited list of strings, or iterable of strings.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            A Grant instance holding access token.
        """
        return await self.fetch_token(
            client_id=client_id,
            grant_type="password",
            scope=scope,
            username=username,
            password=password,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
        )

    async def oidc_authorization_code_grant(
        self,
        client_id: str,
        code: str,
        redirect_uri: str,
        state: t.Optional[str] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> Credentials:
        """Send an authorization code grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        This method is mostly useful when an HTTP server is listening for requests.

        Arguments:
            client_id: OIDC client ID.
            code: The value of authorization code received as request query param.
            redirect_uri: The exact redirect URI used when generating the authorization URL visited to obtain authorization code.
            state: An opaque value used by the client to maintain state between the request and callback.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            A Grant instance holding access token.
        """
        optional_parameters: t.Dict[str, t.Any] = {}
        if state:
            optional_parameters["state"] = state
        return await self.fetch_token(
            client_id=client_id,
            grant_type="authorization_code",
            code=code,
            redirect_uri=redirect_uri,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
            **optional_parameters,
        )

    async def oidc_refresh_token_grant(
        self,
        client_id: str,
        refresh_token: t.Union[str, Credentials],
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> Credentials:
        """Send a refresh token grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        This method should not be used for used for access tokens retrieved from client_credentials grant according to RFC6749 (Section 4.4.3).

        Arguments:
            client_id: OIDC client ID.
            refresh_token: The value of the refresh token.
            scope: Space delimited list of strings, or iterable of strings.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            A Grant instance holding access token.
        """
        if isinstance(refresh_token, Credentials):
            _refresh_token = refresh_token.raw.refresh_token
            if _refresh_token is None:
                raise ValueError("refresh_token argument must be provided")
            refresh_token = _refresh_token
        return await self.fetch_token(
            client_id=client_id,
            grant_type="refresh_token",
            refresh_token=refresh_token,
            scope=scope,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
        )

    async def oidc_client_credentials_grant(
        self,
        client_id: str,
        client_secret: str,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> Credentials:
        """Send a client credential grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        Arguments:
            client_id: OIDC client ID.
            client_secret: The value of the OIDC client secret.
            scope: Space delimited list of strings, or iterable of strings.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        Returns:
            A Grant instance holding access token.
        """
        return await self.fetch_token(
            client_id=client_id,
            grant_type="client_credentials",
            client_secret=client_secret,
            scope=scope,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
        )

    @contextlib.asynccontextmanager
    async def oidc_device_authorization_grant(
        self,
        client_id: str,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
    ) -> t.AsyncIterator[PendingDeviceAuthorization]:
        scope = write_scope(scope, default_scopes=self.default_scopes)
        response = await self._request(
            "POST",
            "device_authorization_endpoint",
            data={
                "client_id": client_id,
                "scope": scope,
            },
        )
        pending_request = PendingDeviceAuthorization(
            **response.json(), pending=PendingCredentials()
        )
        request_deadline = time.time() + pending_request.expires_in
        # Let caller do whatever with the device authorization form
        yield pending_request
        # Once caller exited context, only if no exceptions occured,
        # Try to fetch token using device authorization grant
        # Retry only when error is one of "authorization_pending" or "slow_down"
        try:
            while time.time() < request_deadline:
                try:
                    creds = await self.fetch_token(
                        client_id,
                        grant_type="urn:ietf:params:oauth:grant-type:device_code",
                        device_code=pending_request.device_code,
                        scope=scope,
                        access_token_audience=access_token_audience,
                        id_token_audience=id_token_audience,
                        verify_audience=verify_audience,
                        verify_signature=verify_signature,
                    )
                except httpx.HTTPStatusError as err:
                    details = err.response.json()
                    if "error" not in details:
                        raise
                    error = details["error"]
                    if error == "authorization_pending":
                        await asyncio.sleep(pending_request.interval)
                        continue
                    elif error == "slow_down":
                        await asyncio.sleep(1)
                        continue
                    else:
                        raise
                else:
                    pending_request.set_credentials(creds)
                    break
        except BaseException as exc:
            pending_request.set_exception(exc)
            raise

    async def oidc_browser_login(
        self,
        client_id: str,
        scope: t.Optional[ScopeType] = None,
        state: t.Optional[str] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
        host: str = "localhost",
        port: t.Optional[int] = None,
        prefix: str = "/_oauth",
    ) -> Credentials:
        """Log in using authorization code grant flow.

        - Start an HTTP server in background
        - Generate an authorization URl according to well-known URI, client ID and scope
        - Open a navigator and visit the authorization URL
        - User can log in using OIDC provider login page
        - User is redirected to a page served by the temporary HTTP server
        - User access token is retrieved from query parameters by the HTTP server
        - Stop the HTTP server
        - Return user access token

        Arguments:
            client_id: OIDC client ID.
            scope: Space delimited list of strings, or iterable of strings.
            state: An opaque value used by the client to maintain state between the request and callback.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.

        """
        # Imports required for browser login only
        import socket
        import webbrowser

        try:
            from uvicorn import Config, Server
        except ModuleNotFoundError:
            warnings.warn(
                "'uvicorn' dependency is required to perform browser login. "
                "It can be installed using pip: 'python3 -m pip install uvicorn'"
            )
            raise

        # Guess free port on the machine
        if port is None:
            sock = socket.socket()
            sock.bind(("localhost", 0))
            port = sock.getsockname()[1]
            sock.close()

        # Make sure prefix starts with a "/"
        if not prefix.startswith("/"):
            prefix = f"/{prefix}"

        bind = f"{host}:{port}"
        redirect_uri = f"http://{bind}{prefix}"

        # Initialize future which will store credentials
        creds_future: "asyncio.Future[Credentials]" = (
            asyncio.get_running_loop().create_future()
        )

        async def extract_token(
            scope: t.Mapping[str, t.Any],
            receive: t.Callable[..., t.Coroutine[None, None, None]],
            send: t.Callable[..., t.Coroutine[None, None, None]],
        ) -> None:
            if scope["type"] != "http":
                return
            if scope["path"] != prefix:
                err = ValueError(f"404 Not Found: {scope['path']}")
                try:
                    raise err
                except ValueError as error:
                    creds_future.set_exception(error)
                await send(
                    {
                        "type": "http.response.start",
                        "status": 404,
                        "headers": [
                            [b"content-type", b"text/plain"],
                        ],
                    }
                )
                await send(
                    {
                        "type": "http.response.body",
                        "body": b"Page not found",
                    }
                )
                return
            try:
                query = scope["query_string"]
                parameters: t.Dict[bytes, t.List[bytes]] = urllib.parse.parse_qs(
                    query, keep_blank_values=True
                )
                code = bytes.decode(parameters[b"code"][0])
            except Exception as error:
                error = ValueError(f"Failed to parse code: {error}")
                creds_future.set_exception(error)
                await send(
                    {
                        "type": "http.response.start",
                        "status": 400,
                        "headers": [
                            [b"content-type", b"text/plain"],
                        ],
                    }
                )
                await send(
                    {
                        "type": "http.response.body",
                        "body": b"Invalid code",
                    }
                )
                return
            try:
                creds = await self.oidc_authorization_code_grant(
                    client_id=client_id,
                    code=code,
                    redirect_uri=redirect_uri,
                    state=state,
                    access_token_audience=access_token_audience,
                    id_token_audience=id_token_audience,
                    verify_audience=verify_audience,
                    verify_signature=verify_signature,
                )
            except httpx.HTTPStatusError as err:
                creds_future.set_exception(err)
                await send(
                    {
                        "type": "http.response.start",
                        "status": 400,
                        "headers": [
                            [
                                b"content-type",
                                err.response.charset_encoding.encode()
                                if err.response.charset_encoding
                                else b"text/plain",
                            ],
                        ],
                    }
                )
                await send(
                    {
                        "type": "http.response.body",
                        "body": err.response.content,
                    }
                )
                raise
            except BaseException as err:
                creds_future.set_exception(err)
                raise

            creds_future.set_result(creds)
            await send(
                {
                    "type": "http.response.start",
                    "status": 200,
                    "headers": [
                        [b"content-type", b"text/plain"],
                    ],
                }
            )
            await send(
                {
                    "type": "http.response.body",
                    "body": b"Successfully logged in. You can close this page.",
                }
            )

        async def serve(
            app: t.Callable[..., t.Coroutine[None, None, None]],
            server_ready: "asyncio.Future[None]",
        ) -> Credentials:

            try:
                config = Config(app=app, host=host, port=port, log_level="critical")
                server = Server(config)
                task = asyncio.create_task(server.serve())
                while not server.started or task.done():
                    await asyncio.sleep(1e-3)
                server_ready.set_result(None)
            except BaseException as err:
                server_ready.set_exception(err)
                raise
            try:
                creds = await creds_future
            finally:
                if not task.done():
                    server.should_exit = True
                    await asyncio.wait([task])
                    del server
            return creds

        server_ready: "asyncio.Future[None]" = asyncio.Future()
        server_task = asyncio.create_task(
            serve(extract_token, server_ready=server_ready)
        )
        await server_ready
        url = self.get_authorization_url(
            client_id=client_id, redirect_uri=redirect_uri, scope=scope, state=state
        )
        webbrowser.open_new(url)
        return await server_task


ClientT = t.TypeVar("ClientT", bound="BaseClientAuthenticator")


class BaseClientAuthenticator:
    def __init__(
        self,
        realm: RealmAuthenticator,
        client_id: str,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
        default_scopes: t.Optional[ScopeType] = None,
    ) -> None:
        self.realm = realm
        self.client_id = client_id
        self.access_token_audience = access_token_audience or "account"
        self.id_token_audience = id_token_audience or self.client_id
        self.verify_audience = verify_audience
        self.verify_signature = verify_signature
        self.default_scopes = read_scope(default_scopes)

    async def start(self) -> None:
        await self.realm.start()

    async def stop(self) -> None:
        await self.realm.stop()

    async def __aenter__(self: ClientT) -> ClientT:
        await self.start()
        return self

    async def __aexit__(
        self,
        exc_type: t.Optional[BaseException] = None,
        exc: t.Optional[BaseException] = None,
        tb: t.Optional[types.TracebackType] = None,
    ) -> None:
        await self.stop()
        return None

    def set_access_token_audience(self: ClientT, audience: str) -> ClientT:
        self.access_token_audience = audience
        return self

    def set_id_token_audience(self: ClientT, audience: str) -> ClientT:
        self.id_token_audience = audience
        return self

    def get_access_token_audience(self, value: t.Optional[str]) -> t.Optional[str]:
        return value or self.access_token_audience

    def get_id_token_audience(self, value: t.Optional[str]) -> t.Optional[str]:
        return value or self.id_token_audience

    def should_verify_signature(self, value: t.Optional[bool]) -> bool:
        if value is None:
            return self.verify_signature
        else:
            return value

    def should_verify_audience(self, value: t.Optional[bool]) -> bool:
        if value is None:
            return self.verify_audience
        else:
            return value

    def decode_access_token(
        self,
        token: str,
        audience: t.Optional[str] = None,
        verify_signature: t.Optional[bool] = None,
        verify_audience: t.Optional[bool] = None,
    ) -> AccessToken:
        """Decode an access token using issuer public key.

        Access token hold informations regarding user identity, just like ID tokens,
        but they also hold authorization information such as:
          - realm access (roles)
          - resource access (roles)
          - scopes

        By default JWT signature is verified and audience is verified.
        """
        return self.realm.decode_access_token(
            token=token,
            audience=self.get_access_token_audience(audience),
            verify_signature=self.should_verify_signature(verify_signature),
            verify_audience=self.should_verify_audience(verify_audience),
        )

    def decode_id_token(
        self,
        token: str,
        audience: t.Optional[str] = None,
        verify_signature: t.Optional[bool] = None,
        verify_audience: t.Optional[bool] = None,
    ) -> IDToken:
        """Decode an ID token using issuer public key.

        ID tokens can be used to prove that user is AUTHENTICATED.
        It holds information regarding IDENTITY of the user.
        They should never be used for authorization purpose.
        Use the access token instead.

        By default JWT signature is verified and audience is verified.
        """
        return self.realm.decode_id_token(
            token=token,
            audience=self.get_id_token_audience(audience),
            verify_signature=self.should_verify_signature(verify_signature),
            verify_audience=self.should_verify_audience(verify_audience),
        )

    async def revoke_session(self, creds: Credentials) -> None:
        await self.realm.revoke_session(self.client_id, creds)

    async def fetch_token(
        self,
        grant_type: str,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
        **kwargs: t.Any,
    ) -> Credentials:
        """Send a request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        Arguments:
            grant_type: One of "authorization_code", "refresh_token", "password", "client_credentials".
            scope: Space delimited list of strings, or iterable of strings.
            access_token_audience: Value to check for access token audience claim. Ignored when verify_audience is False.
            id_token_audience: Value to check for id token audience claim. Ignored when verify_audience is False.
            verify_signature: Do not verify the JWT signature when False. True by default.
            verify_audience: Do no verify the access token audience when False. True by default.
            kwargs: Extra arguments specific to each grant type.

        Returns:
            A Grant instance holding access token.
        """
        return await self.realm.fetch_token(
            client_id=self.client_id,
            grant_type=grant_type,
            scope=write_scope(scope, self.default_scopes),
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
            **kwargs,
        )

    async def fetch_user_infos(
        self, access_token: t.Union[str, Credentials]
    ) -> t.Dict[str, t.Any]:
        return await self.realm.fetch_user_infos(access_token)


class PublicClientAuthenticator(BaseClientAuthenticator):
    def __init__(
        self,
        realm: RealmAuthenticator,
        client_id: str,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
        default_scopes: t.Optional[ScopeType] = None,
    ) -> None:
        super().__init__(
            realm=realm,
            client_id=client_id,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
            default_scopes=default_scopes,
        )

    async def revoke_access_token(
        self,
        access_token: t.Union[str, Credentials],
    ) -> None:
        return await self.realm.revoke_access_token(
            self.client_id,
            access_token=access_token,
        )

    async def revoke_refresh_token(
        self,
        refresh_token: t.Union[str, Credentials],
        access_token: t.Union[None, str, Credentials] = None,
    ) -> None:
        return await self.realm.revoke_refresh_token(
            self.client_id,
            refresh_token=refresh_token,
            access_token=access_token,
        )

    async def revoke_session(
        self,
        refresh_token: t.Union[str, Credentials],
        access_token: t.Union[None, str, Credentials] = None,
    ) -> None:
        return await self.realm.revoke_session(
            self.client_id,
            refresh_token=refresh_token,
            access_token=access_token,
        )

    async def oidc_password_grant(
        self,
        username: str,
        password: str,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
    ) -> Credentials:
        """Send a password grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        Arguments:
            username: Name of user.
            password: Password of user.
            scope: Space delimited list of strings, or iterable of strings.

        Returns:
            A Grant instance holding access token.
        """
        return await self.realm.oidc_password_grant(
            client_id=self.client_id,
            username=username,
            password=password,
            scope=write_scope(scope, self.default_scopes),
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
        )

    async def oidc_authorization_code_grant(
        self,
        code: str,
        redirect_uri: str,
        state: t.Optional[str] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
    ) -> Credentials:
        """Send an authorization code grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        This method is mostly useful when an HTTP server is listening for requests.

        Arguments:
            code: The value of authorization code received as request query param.
            redirect_uri: The exact redirect URI used when generating the authorization URL visited to obtain authorization code.

        Returns:
            A Grant instance holding access token.
        """
        return await self.realm.oidc_authorization_code_grant(
            client_id=self.client_id,
            code=code,
            state=state,
            redirect_uri=redirect_uri,
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
        )

    async def oidc_refresh_token_grant(
        self,
        refresh_token: t.Union[str, Credentials],
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
    ) -> Credentials:
        """Send a refresh token grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        This method should not be used for used for access tokens retrieved from client_credentials grant according to RFC6749 (Section 4.4.3).

        Arguments:
            refresh_token: The value of the refresh token.
            scope: Space delimited list of strings, or iterable of strings.

        Returns:
            A Grant instance holding access token.
        """
        return await self.realm.oidc_refresh_token_grant(
            client_id=self.client_id,
            refresh_token=refresh_token,
            scope=write_scope(scope, self.default_scopes),
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
        )

    def oidc_device_authorization_grant(
        self,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
    ) -> t.AsyncContextManager[PendingDeviceAuthorization]:
        return self.realm.oidc_device_authorization_grant(
            self.client_id,
            scope=write_scope(scope, self.default_scopes),
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
        )

    async def oidc_browser_login(
        self,
        scope: t.Optional[ScopeType] = None,
        state: t.Optional[str] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
        host: str = "localhost",
        port: int = 8000,
    ) -> Credentials:
        """Log in using authorization code grant flow.

        - Start an HTTP server in background
        - Generate an authorization URl according to well-known URI, client ID and scope
        - Open a navigator and visit the authorization URL
        - User can log in using OIDC provider login page
        - User is redirected to a page served by the temporary HTTP server
        - User access token is retrieved from query parameters by the HTTP server
        - Stop the HTTP server
        - Return user access token

        Arguments:
            scope: Optional OIDC scope.

        """
        return await self.realm.oidc_browser_login(
            client_id=self.client_id,
            scope=write_scope(scope, self.default_scopes),
            state=state,
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
            host=host,
            port=port,
        )

    @classmethod
    def from_env(
        cls,
        client_id_env: str = "OIDC_CLIENT_ID",
        well_known_uri_env: str = "OIDC_WELL_KNOWN_URI",
        access_token_audience_env: str = "OIDC_ACCESS_TOKEN_AUDIENCE",
        id_token_audience_env: str = "OIDC_ID_TOKEN_AUDIENCE",
        verify_signature_env: str = "OIDC_VERIFY_SIGNATURE",
        verify_audience_env: str = "OIDC_VERIFY_AUDIENCE",
        default_scopes_env: str = "OIDC_DEFAULT_SCOPES",
    ) -> "PublicClientAuthenticator":
        try:
            well_known_uri = os.environ[well_known_uri_env]
        except KeyError:
            raise KeyError(f"Environment variable {well_known_uri_env} is not set")
        try:
            client_id = os.environ[client_id_env]
        except KeyError:
            raise KeyError(f"Environment variable {client_id_env} is not set")
        return cls(
            realm=RealmAuthenticator(
                well_known_uri=well_known_uri,
                default_scopes=read_scope(
                    os.environ.get(default_scopes_env, DEFAULT_SCOPES)
                ),
            ),
            client_id=client_id,
            access_token_audience=os.environ.get(access_token_audience_env, None),
            id_token_audience=os.environ.get(id_token_audience_env, None),
            verify_audience=bool_validator(os.environ.get(verify_audience_env, "1")),
            verify_signature=bool_validator(os.environ.get(verify_signature_env, "1")),
        )


class ConfidentialClientAuthenticator(BaseClientAuthenticator):
    def __init__(
        self,
        realm: RealmAuthenticator,
        client_id: str,
        client_secret: str,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: bool = True,
        verify_signature: bool = True,
        default_scopes: t.Optional[ScopeType] = None,
    ) -> None:
        super().__init__(
            realm=realm,
            client_id=client_id,
            access_token_audience=access_token_audience,
            id_token_audience=id_token_audience,
            verify_audience=verify_audience,
            verify_signature=verify_signature,
            default_scopes=default_scopes,
        )
        self.client_secret = client_secret

    async def introspect_token(
        self, access_token: t.Union[str, Credentials]
    ) -> t.Dict[str, t.Any]:
        return await self.realm.introspect_token(
            self.client_id,
            access_token=access_token,
            client_secret=self.client_secret,
        )

    async def revoke_access_token(
        self,
        access_token: t.Union[str, Credentials],
    ) -> None:
        return await self.realm.revoke_access_token(
            self.client_id,
            access_token=access_token,
            client_secret=self.client_secret,
        )

    async def oidc_client_credentials_grant(
        self,
        scope: t.Optional[ScopeType] = None,
        access_token_audience: t.Optional[str] = None,
        id_token_audience: t.Optional[str] = None,
        verify_audience: t.Optional[bool] = None,
        verify_signature: t.Optional[bool] = None,
    ) -> Credentials:
        """Send a client credential grant request to the token endpoint to obtain an access token, an ID token, and optionally a refresh token.

        Arguments:
            client_id: OIDC client ID.
            client_secret: The value of the OIDC client secret.
            scope: Space delimited list of strings, or iterable of strings.

        Returns:
            A Grant instance holding access token.
        """
        return await self.fetch_token(
            grant_type="client_credentials",
            client_secret=self.client_secret,
            scope=write_scope(scope, self.default_scopes),
            access_token_audience=self.get_access_token_audience(access_token_audience),
            id_token_audience=self.get_id_token_audience(id_token_audience),
            verify_audience=self.should_verify_audience(verify_audience),
            verify_signature=self.should_verify_signature(verify_signature),
        )

    @classmethod
    def from_env(
        cls,
        client_id_env: str = "OIDC_CLIENT_ID",
        client_secret_env: str = "OIDC_CLIENT_SECRET",
        well_known_uri_env: str = "OIDC_WELL_KNOWN_URI",
        access_token_audience_env: str = "OIDC_ACCESS_TOKEN_AUDIENCE",
        id_token_audience_env: str = "OIDC_ID_TOKEN_AUDIENCE",
        verify_signature_env: str = "OIDC_VERIFY_SIGNATURE",
        verify_audience_env: str = "OIDC_VERIFY_AUDIENCE",
        default_scopes_env: str = "OIDC_DEFAULT_SCOPES",
    ) -> "ConfidentialClientAuthenticator":
        try:
            well_known_uri = os.environ[well_known_uri_env]
        except KeyError:
            raise KeyError(f"Environment variable {well_known_uri_env} is not set")
        try:
            client_id = os.environ[client_id_env]
        except KeyError:
            raise KeyError(f"Environment variable {client_id_env} is not set")
        try:
            client_secret = os.environ[client_secret_env]
        except KeyError:
            raise KeyError(f"Environment variable {client_secret_env} is not set")
        return cls(
            realm=RealmAuthenticator(
                well_known_uri=well_known_uri,
                default_scopes=read_scope(
                    os.environ.get(default_scopes_env, DEFAULT_SCOPES)
                ),
            ),
            client_id=client_id,
            client_secret=client_secret,
            access_token_audience=os.environ.get(access_token_audience_env, None),
            id_token_audience=os.environ.get(id_token_audience_env, None),
            verify_audience=bool_validator(os.environ.get(verify_audience_env, "1")),
            verify_signature=bool_validator(os.environ.get(verify_signature_env, "1")),
        )


if __name__ == "__main__":
    # Create an RealmAuthenticator
    auth = RealmAuthenticator(well_known_uri=DEFAULT_WELL_KNOWN)
    # Create a client
    client = auth.get_public_client("quara-cli")

    async def main() -> Credentials:
        """Test to obtain OIDC JWT using RealmAuthenticator client."""
        async with client:
            # Login using a browser
            creds = await client.oidc_browser_login()

            # Login using user/pass
            # creds = await client.oidc_password_grant(
            #     username="USERNAME", password="PASSWORD"
            # )

            # Login using device code
            # While context manager is not closed, request is pending.
            async with client.oidc_device_authorization_grant() as pending:
                print(
                    f"Go to {pending.verification_uri} and enter the code: {pending.user_code}"
                )
            # Get credentials from pending request
            creds = pending.get_credentials()

            # Login using client credentials
            # creds = await client.oidc_client_credentials_grant(client_secret="SECRET")

            # Login using refresh token
            return await client.oidc_refresh_token_grant(creds)
