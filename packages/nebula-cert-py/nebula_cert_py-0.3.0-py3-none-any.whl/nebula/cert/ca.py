from __future__ import annotations

import json
import tempfile
import typing as t
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from subprocess import check_call, check_output

from dateutil.parser import parse as parse_datetime


@dataclass
class CAOptions:
    """Options used to create a new Certificate Authority"""

    name: str
    ips: t.List[str] = field(default_factory=list)
    duration: str = "25950h"  # 3 years
    subnets: t.List[str] = field(default_factory=list)
    groups: t.List[str] = field(default_factory=list)


@dataclass
class SignRequestTemplate:
    """Options used to sign a new certificate for a nebula node"""

    ip: str
    duration: str = "8650h"  # 1 year
    subnets: t.List[str] = field(default_factory=list)
    groups: t.List[str] = field(default_factory=list)

    def get_options(self, name: str) -> SignRequestOptions:
        return SignRequestOptions(name=name, **asdict(self))


@dataclass
class SignRequestOptions:
    """Options used to sign a new certificate for a nebula node"""

    name: str
    ip: str
    duration: str = "8650h"  # 1 year
    subnets: t.List[str] = field(default_factory=list)
    groups: t.List[str] = field(default_factory=list)


@dataclass
class CertificateDetails:
    """Details about a Nebula certificate"""

    groups: t.List[str]
    ips: t.List[str]
    isCa: bool
    issuer: str
    name: str
    notAfter: str
    notBefore: str
    publicKey: str
    subnets: t.List[str]


@dataclass
class Certificate:
    """Nebula certificate"""

    raw: bytes
    details: CertificateDetails
    fingerprint: str
    signature: str
    expiration_timestamp: datetime = field(init=False)
    start_timestamp: datetime = field(init=False)

    def __post_init__(self) -> None:
        """Automatically set expiration_timestamp and start_timestamp according to details"""
        if isinstance(self.details, dict):
            self.details = CertificateDetails(**self.details)
        try:
            self.expiration_timestamp = datetime.fromisoformat(self.details.notAfter)
        except (TypeError, ValueError):
            self.expiration_timestamp = parse_datetime(self.details.notAfter)
        try:
            self.start_timestamp = datetime.fromisoformat(self.details.notBefore)
        except (TypeError, ValueError):
            self.start_timestamp = parse_datetime(self.details.notBefore)

    @classmethod
    def from_file(cls, path: t.Union[str, Path]) -> Certificate:
        """Parse a certificate"""
        cert_file = Path(path).expanduser()
        if not cert_file.exists():
            raise FileNotFoundError(cert_file.as_posix())
        output = check_output(
            ["nebula-cert", "print", "-path", cert_file.as_posix(), "-json"]
        ).strip()
        return cls(**json.loads(output), raw=cert_file.read_bytes())

    @classmethod
    def from_bytes(cls, data: bytes) -> Certificate:
        """Parse a certificate"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cert_file = Path(tmpdir, "crt")
            cert_file.write_bytes(data)
            output = check_output(
                ["nebula-cert", "print", "-path", cert_file.as_posix(), "-json"]
            ).strip()
            return cls(**json.loads(output), raw=data)

    def as_string(self) -> str:
        return self.raw.decode("utf-8")


class PublicKey:
    def __init__(self, value: t.Union[str, bytes, PublicKey]) -> None:
        if isinstance(value, PublicKey):
            str_value = value.as_long_string()
        elif isinstance(value, bytes):
            str_value = value.decode("utf-8")
        else:
            str_value = value
        if not str_value.startswith("-----"):
            str_value = "\n".join(
                [
                    "-----BEGIN NEBULA X25519 PUBLIC KEY-----",
                    str_value,
                    "-----END NEBULA X25519 PUBLIC KEY-----",
                ]
            )
        self._value = str_value

    def as_short_string(self) -> str:
        return self._value.splitlines(False)[1].strip()

    def as_long_string(self) -> str:
        return self._value

    def as_bytes(self) -> bytes:
        return self._value.encode("utf-8")

    @classmethod
    def from_file(cls, filepath: t.Union[str, Path]) -> PublicKey:
        return cls(Path(filepath).expanduser().read_bytes())

    def __eq__(self, other: t.Any) -> bool:
        if isinstance(other, str):
            return other == self._value
        if isinstance(other, bytes):
            return other == self.as_bytes()
        if isinstance(other, PublicKey):
            return other._value == self._value
        return False

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f'PublicKey("{self.as_short_string()}")'


class PrivateKey:
    def __init__(self, value: t.Union[str, bytes, PrivateKey]) -> None:
        if isinstance(value, PrivateKey):
            str_value = value.as_long_string()
        elif isinstance(value, bytes):
            str_value = value.decode("utf-8")
        else:
            str_value = value
        if not str_value.startswith("-----"):
            str_value = "\n".join(
                [
                    "-----BEGIN NEBULA X25519 PRIVATE KEY-----",
                    str_value,
                    "-----END NEBULA X25519 PRIVATE KEY-----",
                ]
            )
        self._value = str_value

    def as_short_string(self) -> str:
        return self._value.splitlines(False)[1].strip()

    def as_long_string(self) -> str:
        return self._value

    def as_bytes(self) -> bytes:
        return self._value.encode("utf-8")

    @classmethod
    def from_file(cls, filepath: t.Union[str, Path]) -> PrivateKey:
        return cls(Path(filepath).expanduser().read_bytes())

    def __eq__(self, other: t.Any) -> bool:
        if isinstance(other, str):
            return other == self._value
        if isinstance(other, bytes):
            return other == self.as_bytes()
        if isinstance(other, PrivateKey):
            return other._value == self._value
        return False

    def __str__(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"PrivateKey(\"{'*' * len(self.as_short_string())}\")"


@dataclass
class KeyPair:
    public_key: PublicKey
    private_key: PrivateKey

    @classmethod
    def from_values(
        cls,
        public_key: t.Union[str, bytes, PublicKey],
        private_key: t.Union[str, bytes, PrivateKey],
    ) -> KeyPair:
        return cls(
            public_key=PublicKey(public_key), private_key=PrivateKey(private_key)
        )

    def write(self, name: str, directory: t.Union[str, Path] = ".") -> Path:
        directory = Path(directory).expanduser() if directory else Path.cwd()
        directory.mkdir(exist_ok=True, parents=True)
        directory.joinpath(name + ".key").write_bytes(self.private_key.as_bytes())
        directory.joinpath(name + ".pub").write_bytes(self.public_key.as_bytes())


@dataclass
class PublicCreds:
    public_key: PublicKey
    cert: Certificate
    qr: t.Optional[bytes] = field(default=None, repr=False)

    @classmethod
    def from_values(
        cls,
        public_key: t.Union[str, bytes, PublicKey],
        cert: t.Union[str, bytes],
        qr: t.Optional[bytes] = None,
    ) -> PublicCreds:
        if isinstance(cert, str):
            cert = cert.encode("utf-8")
        certificate = Certificate.from_bytes(cert)
        public_key = PublicKey(public_key)
        return cls(
            public_key=public_key,
            cert=certificate,
            qr=qr,
        )

    @classmethod
    def from_files(
        cls,
        public_key_file: t.Union[str, Path],
        cert_file: t.Union[str, Path],
        qr_file: t.Union[None, str, Path] = None,
    ) -> PublicCreds:
        certificate = Certificate.from_file(cert_file)
        pub_key = PublicKey.from_file(public_key_file)
        if qr_file:
            try:
                qr = Path(qr_file).read_bytes()
            except FileNotFoundError:
                qr = None
        return cls(public_key=pub_key, cert=certificate, qr=qr)

    @classmethod
    def from_directory(
        cls,
        directory: t.Union[str, Path],
        filename: str,
    ) -> PublicCreds:
        crt_file = Path(directory, f"{filename}.crt")
        public_key_file = Path(directory, f"{filename}.pub")
        qr_file = Path(directory, f"{filename}.png")
        return cls.from_files(
            public_key_file=public_key_file, cert_file=crt_file, qr_file=qr_file
        )

    def write(self, name: str, directory: t.Union[str, Path, None] = None) -> Path:
        """Write certificate to files"""
        directory = Path(directory).expanduser() if directory else Path.cwd()
        directory.mkdir(exist_ok=True, parents=True)
        directory.joinpath(name + ".crt").write_bytes(self.cert.raw)
        directory.joinpath(name + ".pub").write_bytes(self.public_key.as_bytes())
        if self.qr:
            directory.joinpath(name + ".png").write_bytes(self.qr)
        return directory

    @contextmanager
    def mkdtemp(self, name: str) -> t.Iterator[Path]:
        """Write certificate, public key and qr code into temporary directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            Path(tmpdir, f"{name}.pub").write_bytes(self.public_key.as_bytes())
            Path(tmpdir, f"{name}.crt").write_bytes(self.cert.raw)
            if self.qr:
                Path(tmpdir, f"{name}.png").write_bytes(self.qr)
            yield Path(tmpdir)


PrivateCredsT = t.TypeVar("PrivateCredsT", bound="PrivateCreds")


@dataclass
class PrivateCreds:
    """Base class for nebula credentials"""

    private_key: PrivateKey
    cert: Certificate
    qr: t.Optional[bytes] = field(default=None, repr=False)
    public_key: t.Optional[PublicKey] = None

    @classmethod
    def from_values(
        cls: t.Type[PrivateCredsT],
        private_key: t.Union[str, bytes, PrivateKey],
        cert: t.Union[str, bytes],
        qr: t.Optional[bytes] = None,
        public_key: t.Union[str, bytes, PublicKey, None] = None,
    ) -> PrivateCredsT:
        """Create a PublicCreds instance according to values given as arguments"""
        if isinstance(cert, str):
            cert = cert.encode("utf-8")
        certificate = Certificate.from_bytes(cert)
        private_key = PrivateKey(private_key)
        if public_key is not None:
            public_key = PublicKey(public_key)
        return cls(
            private_key=private_key,
            cert=certificate,
            public_key=public_key,
            qr=qr,
        )

    @classmethod
    def from_files(
        cls: t.Type[PrivateCredsT],
        private_key_file: t.Union[str, Path],
        cert_file: t.Union[str, Path],
        qr_file: t.Union[None, str, Path] = None,
        public_key_file: t.Union[str, Path, None] = None,
    ) -> PrivateCredsT:
        certificate = Certificate.from_file(cert_file)
        private_key = PrivateKey.from_file(private_key_file)
        try:
            if public_key_file:
                public_key = PublicKey.from_file(public_key_file)
            else:
                public_key = None
        except FileNotFoundError:
            public_key = None
        try:
            if qr_file:
                qr = Path(qr_file).read_bytes()
            else:
                qr = None
        except FileNotFoundError:
            qr = None
        return cls(
            private_key=private_key, cert=certificate, qr=qr, public_key=public_key
        )

    @classmethod
    def from_directory(
        cls: t.Type[PrivateCredsT], directory: t.Union[str, Path], name: str
    ) -> PrivateCredsT:
        """Create a credential instance according to files found in directory"""
        cert_file = Path(directory, f"{name}.crt")
        pub_file = Path(directory, f"{name}.pub")
        key_file = Path(directory, f"{name}.key")
        qr_file = Path(directory, f"{name}.png")
        return cls.from_files(
            private_key_file=key_file,
            cert_file=cert_file,
            qr_file=qr_file,
            public_key_file=pub_file,
        )

    def write(self, name: str, directory: t.Union[str, Path, None] = None) -> Path:
        """Write certificate and key to files"""
        directory = Path(directory).expanduser() if directory else Path.cwd()
        directory.mkdir(parents=True, exist_ok=True)
        directory.joinpath(name + ".key").write_bytes(self.private_key.as_bytes())
        directory.joinpath(name + ".crt").write_bytes(self.cert.raw)
        if self.public_key:
            directory.joinpath(name + ".pub").write_bytes(self.public_key.as_bytes())
        if self.qr:
            directory.joinpath(name + ".png").write_bytes(self.qr)
        return directory

    @contextmanager
    def mkdtemp(self, name: str) -> t.Iterator[Path]:
        """Write certificate, private key and qr code into temporary directory"""
        with tempfile.TemporaryDirectory() as tmpdir:
            Path(tmpdir, f"{name}.key").write_bytes(self.private_key.as_bytes())
            Path(tmpdir, f"{name}.crt").write_bytes(self.cert.raw)
            if self.public_key:
                Path(tmpdir, f"{name}.pub").write_bytes(self.public_key.as_bytes())
            if self.qr:
                Path(tmpdir, f"{name}.png").write_bytes(self.qr)
            yield Path(tmpdir)


@dataclass
class CA(PrivateCreds):
    @classmethod
    def from_files(  # type: ignore[override]
        cls,
        private_key_file: t.Union[str, Path] = "ca.key",
        cert_file: t.Union[str, Path] = "ca.crt",
        qr_file: t.Union[None, str, Path] = "ca.png",
    ) -> CA:
        return super().from_files(
            private_key_file=private_key_file, cert_file=cert_file, qr_file=qr_file
        )

    @classmethod
    def from_directory(cls, directory: t.Union[str, Path], name: str = "ca") -> CA:
        return super().from_directory(directory, name)

    def write(
        self, name: str = "ca", directory: t.Union[str, Path, None] = None
    ) -> Path:
        return super().write(name, directory)

    @contextmanager
    def mkdtemp(self, name: str = "ca") -> t.Iterator[Path]:
        """Enter temporary directory where it's possible to sign certificates"""
        with super().mkdtemp(name) as directory:
            yield directory

    @staticmethod
    def _create_keypair_cmd(public_key_file: str, private_key_file: str) -> t.List[str]:
        return [
            "nebula-cert",
            "keygen",
            "-out-key",
            private_key_file,
            "-out-pub",
            public_key_file,
        ]

    @staticmethod
    def _create_ca_cmd(options: CAOptions, filename: str = "ca") -> t.List[str]:
        args: t.List[str] = [
            "-name",
            options.name,
            "-duration",
            options.duration,
            "-out-qr",
            f"{filename}.png",
            "-out-key",
            f"{filename}.key",
            "-out-crt",
            f"{filename}.crt",
        ]
        if options.ips:
            args += ["-ips", ",".join(options.ips)]
        if options.subnets:
            args += ["-subnets", ",".join(options.subnets)]
        if options.groups:
            args += ["-groups", ",".join(options.groups)]

        return ["nebula-cert", "ca", *args]

    @staticmethod
    def _sign_cert_cmd(options: SignRequestOptions, filename: str) -> t.List[str]:
        args = [
            "-duration",
            options.duration,
            "-name",
            options.name,
            "-ip",
            options.ip,
            "-out-crt",
            f"{filename}.crt",
            "-in-pub",
            f"{filename}.pub",
            "-out-qr",
            f"{filename}.png",
        ]
        if options.subnets:
            args += ["-subnets", ",".join(options.subnets)]
        if options.groups:
            args += ["-groups", ",".join(options.groups)]

        return ["nebula-cert", "sign", *args]

    def sign_certificate(
        self,
        public_key: t.Union[str, PublicKey],
        options: t.Union[t.Mapping[str, t.Any], SignRequestOptions],
    ) -> PublicCreds:

        if not isinstance(public_key, PublicKey):
            public_key = PublicKey(public_key)

        if not isinstance(options, SignRequestOptions):
            options = SignRequestOptions(**options)

        cmd = self._sign_cert_cmd(options, filename="out")

        with self.mkdtemp() as tmpdir:
            Path(tmpdir).joinpath("out.pub").write_bytes(public_key.as_bytes())
            # Generate certificates
            check_call(cmd, cwd=tmpdir)
            # Parse certificate from files
            return PublicCreds.from_directory(tmpdir, filename="out")

    def create_certificate(
        self, options: t.Union[SignRequestOptions, t.Mapping[str, t.Any]]
    ) -> PrivateCreds:
        if not isinstance(options, SignRequestOptions):
            options = SignRequestOptions(**options)
        keypair = self.create_keypair()
        host = Host(
            name=options.name,
            public_key=keypair.public_key,
            private_key=keypair.private_key,
            sign_requests=[options],
            typ="user",
        )
        public_creds = self.sign_certificate(host.public_key, options)
        return PrivateCreds(
            private_key=keypair.private_key,
            cert=public_creds.cert,
            qr=public_creds.qr,
            public_key=keypair.public_key,
        )

    @classmethod
    def create_ca(cls, options: t.Union[CAOptions, t.Mapping[str, t.Any]]) -> CA:
        if not isinstance(options, CAOptions):
            options = CAOptions(**options)
        # Gather command used to create CA
        cmd = cls._create_ca_cmd(options)
        # Enter temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            # Create cert
            check_call(cmd, cwd=tmpdir)
            # Gather results
            certificate = Certificate.from_file(root / "ca.crt")
            private_key = PrivateKey.from_file(root / "ca.key")
            try:
                ca_qr = Path(tmpdir, "ca.png").read_bytes()
            except FileNotFoundError:
                ca_qr = None
        # Return certificate
        return CA(private_key=private_key, cert=certificate, qr=ca_qr)

    @classmethod
    def create_keypair(cls) -> KeyPair:
        # Gather command used to create CA
        cmd = cls._create_keypair_cmd("public_key", "private_key")
        # Enter temporary directory
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            # Create cert
            check_call(cmd, cwd=tmpdir)
            # Gather results
            public_key = PublicKey.from_file(root / "public_key")
            private_key = PrivateKey.from_file(root / "private_key")
        return KeyPair(public_key=public_key, private_key=private_key)

    @classmethod
    def from_keyvault(
        cls, keyvault_name: str, cert_name: str, key_name: str, creds: t.Any = None
    ) -> CA:
        """Store CA cert and CA key into Azure Keyvault"""
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.secrets import SecretClient

        uri = f"https://{keyvault_name}.vault.azure.net"
        if creds is None:
            creds = DefaultAzureCredential(
                exclude_environment_credential=True,
                exclude_interactive_browser_credential=False,
            )
        secrets_client = SecretClient(vault_url=uri, credential=creds)
        cert = secrets_client.get_secret(name=cert_name)
        key = secrets_client.get_secret(name=key_name)
        return cls.from_values(key.value, cert.value)

    def to_keyvault(
        self, keyvault_name: str, cert_name: str, key_name: str, creds: t.Any = None
    ) -> None:
        """Store CA cert and CA key into Azure Keyvault"""
        from azure.identity import DefaultAzureCredential
        from azure.keyvault.secrets import SecretClient

        uri = f"https://{keyvault_name}.vault.azure.net"
        if creds is None:
            creds = DefaultAzureCredential()
        secrets_client = SecretClient(vault_url=uri, credential=creds)
        secrets_client.set_secret(cert_name, self.cert.as_string())
        secrets_client.set_secret(key_name, self.private_key.as_long_string())


@dataclass
class Host:
    name: str
    public_key: t.Optional[PublicKey] = None
    private_key: t.Optional[PrivateKey] = None
    sign_requests: t.List[SignRequestTemplate] = field(default_factory=list)
    typ: str = ""

    def __post_init__(self) -> None:
        if self.typ not in ("server", "user"):
            raise TypeError(f"Invalid host type: {self.typ}")

    def to_dict(
        self, exclude_public_key: bool = True, exclude_private_key: bool = True
    ) -> t.Dict[str, t.Any]:
        data = {
            "name": self.name,
            "sign_requests": [asdict(request) for request in self.sign_requests],
            "typ": self.typ,
        }
        if not exclude_public_key and self.public_key:
            data["public_key"] = self.public_key.as_long_string()
        if not exclude_private_key and self.private_key:
            data["private_key"] = self.private_key.as_long_string()
        return data

    def get_ip_addresses(self) -> t.List[str]:
        """Return all IP addresses owned by host"""
        return [options.ip for options in self.sign_requests]

    @classmethod
    def from_values(
        cls,
        name: str,
        typ: str,
        public_key: t.Union[None, PublicKey, str, bytes] = None,
        private_key: t.Union[None, PrivateKey, str, bytes] = None,
        sign_requests: t.Optional[
            t.Iterable[t.Union[t.Mapping[str, t.Any], SignRequestTemplate]]
        ] = None,
    ) -> Host:
        sign_requests_list = (
            [
                request
                if isinstance(request, SignRequestTemplate)
                else SignRequestTemplate(**request)
                for request in sign_requests
            ]
            if sign_requests
            else []
        )
        if typ == "user":
            return User(
                name=name,
                public_key=PublicKey(public_key) if public_key else None,
                private_key=PrivateKey(private_key) if private_key else None,
                typ=typ,
                sign_requests=sign_requests_list,
            )
        elif typ == "server":
            return Server(
                name=name,
                public_key=PublicKey(public_key) if public_key else None,
                private_key=PrivateKey(private_key) if private_key else None,
                typ=typ,
                sign_requests=sign_requests_list,
            )
        else:
            return cls(
                name=name,
                public_key=PublicKey(public_key) if public_key else None,
                private_key=PrivateKey(private_key) if private_key else None,
                typ=typ,
                sign_requests=sign_requests_list,
            )

    @classmethod
    def from_files(cls, directory: t.Union[str, Path] = "~/.nebula") -> "Host":
        directory = Path(directory).expanduser()
        host = Host.from_values(
            **json.loads(directory.joinpath("config.json").read_bytes())
        )
        if host.public_key is None:
            host.public_key = PublicKey.from_file(directory.joinpath("node.pub"))
        if host.private_key is None:
            try:
                host.private_key = PrivateKey.from_file(directory.joinpath("node.key"))
            except FileNotFoundError:
                pass
        return host

    def save_files(self, directory: t.Union[str, Path] = "~/.nebula") -> Path:
        directory = Path(directory).expanduser()
        directory.mkdir(exist_ok=True, parents=True)
        config = self.to_dict(exclude_public_key=True, exclude_private_key=True)
        directory.joinpath("config.json").write_bytes(
            json.dumps(config).encode("utf-8")
        )
        if self.public_key:
            directory.joinpath("node.pub").write_bytes(self.public_key.as_bytes())
        if self.private_key:
            directory.joinpath("node.key").write_bytes(self.private_key.as_bytes())


@dataclass
class Server(Host):
    typ: str = "server"

    def __post_init__(self) -> None:
        self.typ = "server"
        super().__post_init__()


@dataclass
class User(Host):
    typ: str = "user"

    def __post_init__(self) -> None:
        self.typ = "user"
        super().__post_init__()


@dataclass
class Catalog:
    servers: t.Dict[str, Server] = field(default_factory=dict)
    users: t.Dict[str, User] = field(default_factory=dict)

    def to_hosts_file(self, filepath: t.Union[str, Path]) -> Path:
        out = Path(filepath)
        out.write_bytes(
            json.dumps(
                [
                    host.to_dict(exclude_public_key=False, exclude_private_key=True)
                    for host in self.get_hosts_list()
                ],
                indent=2,
            ).encode("utf-8")
        )
        return out

    @classmethod
    def from_hosts_file(cls, filepath: t.Union[str, Path]) -> Catalog:
        hosts = json.loads(Path(filepath).expanduser().read_bytes())
        return cls.from_hosts(hosts)

    @classmethod
    def from_hosts(
        cls,
        hosts: t.Union[
            t.Mapping[str, t.Union[Server, User, t.Dict[str, t.Any]]],
            t.Iterable[t.Union[Server, User, t.Dict[str, t.Any]]],
        ],
    ) -> Catalog:
        """Create a catalog out of an iterable of hosts (either Server or User)"""
        catalog = Catalog()
        if isinstance(hosts, t.Mapping):
            hosts = hosts.values()
        for host in hosts:
            if not isinstance(host, Host):
                host = Host.from_values(**host)
            if isinstance(host, User):
                catalog.users[host.name] = host
            elif isinstance(host, Server):
                catalog.servers[host.name] = host
            else:
                raise TypeError(f"Invalid host type: {host.typ}")
        return catalog

    def get_hosts_list(self) -> t.List[t.Union[User, Server]]:
        hosts: t.List[t.Union[User, Server]] = list(self.users.values())
        hosts.extend(self.servers.values())
        return hosts

    def get_hosts_dict(self) -> t.Dict[str, Host]:
        hosts: t.Dict[str, Host]
        hosts = dict(self.users.copy())
        hosts.update(self.servers)
        return hosts

    def get_host(
        self, name: str, typ: t.Optional[str] = None
    ) -> t.Union[Host, Server, User]:
        if typ is None:
            return self.get_hosts_dict()[name]
        elif typ == "user":
            return self.users[name]
        elif typ == "server":
            return self.servers[name]
        else:
            raise TypeError(f"Invalid host type: {typ}")

    def get_host_by_ip(
        self, ip: str, typ: t.Optional[str] = None
    ) -> t.Union[Host, Server, User]:
        hosts: t.Iterable[Host]
        if typ is None:
            hosts = self.get_hosts_list()
        elif typ == "user":
            hosts = self.users.values()
        elif typ == "servers":
            hosts = self.servers.values()
        else:
            raise TypeError(f"Invalid host typ: {typ}")
        for host in hosts:
            if ip in host.get_ip_addresses():
                return host
        raise KeyError(f"No host with ip {ip}")

    def get_host_by_public_key(
        self, public_key: str, typ: t.Optional[str] = None
    ) -> t.Union[Host, Server, User]:
        expected = PublicKey(public_key)
        hosts: t.Iterable[Host]
        if typ is None:
            hosts = self.get_hosts_list()
        elif typ == "user":
            hosts = self.users.values()
        elif typ == "servers":
            hosts = self.servers.values()
        else:
            raise TypeError(f"Invalid host typ: {typ}")
        for host in hosts:
            if host.public_key == expected:
                return host
        raise KeyError(f"No host with public key {public_key}")

    def get_user(self, name: str) -> User:
        return t.cast(User, self.get_host(name, typ="user"))

    def get_user_by_ip(self, ip: str) -> User:
        return t.cast(User, self.get_host_by_ip(ip, typ="user"))

    def get_user_by_public_key(self, public_key: str) -> User:
        return t.cast(User, self.get_host_by_public_key(public_key, typ="user"))

    def get_server(self, name: str) -> Server:
        return t.cast(Server, self.get_host(name, typ="server"))

    def get_server_by_ip(self, ip: str) -> Server:
        return t.cast(Server, self.get_host_by_ip(ip, typ="server"))

    def get_server_by_public_key(self, public_key: str) -> Server:
        return t.cast(Server, self.get_host_by_public_key(public_key, typ="user"))

    def get_all_ips(self) -> t.List[str]:
        addresses: t.Set[str] = set()
        for host in self.get_hosts_list():
            addresses.update([options.ip for options in host.sign_requests])
        return sorted(addresses)


class Manager:
    def __init__(
        self,
        ca: CA,
        catalog: t.Union[str, Path, Catalog] = None,
        store: t.Union[str, Path] = "./creds",
    ) -> None:
        self.ca = ca
        if isinstance(catalog, (str, Path)):
            catalog = Catalog.from_hosts_file(catalog)
        self.catalog = catalog or Catalog()
        self.store = Path(store)
        self.users_store = self.store / "users"
        self.servers_store = self.store / "servers"
        self.users_store.mkdir(exist_ok=True, parents=True)
        self.servers_store.mkdir(exist_ok=True)

    def sign_host(
        self, name: str, typ: t.Optional[str] = None
    ) -> t.Iterator[PublicCreds]:
        host = self.catalog.get_host(name, typ=typ)
        if host.public_key is None:
            raise ValueError(
                "Missing private key. Use create_and_sign_host method instead."
            )
        for options in host.sign_requests:
            creds = self.ca.sign_certificate(host.public_key, options.get_options(name))
            if host.typ == "user":
                creds.write(host.name, self.users_store.joinpath(name))
            elif host.typ == "server":
                creds.write(host.name, self.servers_store.joinpath(name))
            else:
                raise TypeError(f"Invalid host typ: {typ}")
            yield creds

    def sign_user(self, name: str) -> t.Iterator[PublicCreds]:
        return self.sign_host(name, typ="user")

    def sign_server(self, name: str) -> t.Iterator[PublicCreds]:
        return self.sign_host(name, typ="server")

    def create_host(
        self,
        name: str,
        typ: str,
        sign_requests: t.Optional[
            t.Iterable[t.Union[SignRequestTemplate, t.Mapping[str, t.Any]]]
        ] = None,
    ) -> t.Iterator[PrivateCreds]:
        keypair = self.ca.create_keypair()
        if typ == "user":
            self.catalog.users[name] = User.from_values(
                name=name,
                typ=typ,
                public_key=keypair.public_key,
                private_key=keypair.private_key,
                sign_requests=sign_requests,
            )
        elif typ == "server":
            self.catalog.servers[name] = Server.from_values(
                name=name,
                typ=typ,
                public_key=keypair.public_key,
                private_key=keypair.private_key,
                sign_requests=sign_requests,
            )
        else:
            raise TypeError(f"Invalid host type: {typ}")

        for template in sign_requests:
            creds = self.ca.sign_certificate(
                keypair.public_key, options=template.get_options(name)
            )
            private_creds = PrivateCreds(
                private_key=keypair.private_key,
                cert=creds.cert,
                qr=creds.qr,
                public_key=creds.public_key,
            )
            if typ == "user":
                private_creds.write(name, self.users_store.joinpath(name))
            else:
                private_creds.write(name, self.servers_store.joinpath(name))
            yield private_creds

    def create_user(
        self,
        name: str,
        sign_requests: t.Optional[
            t.Iterable[t.Union[SignRequestTemplate, t.Mapping[str, t.Any]]]
        ] = None,
    ) -> t.Iterator[PrivateCreds]:
        return self.create_host(name, typ="user", sign_requests=sign_requests)

    def create_server(
        self,
        name: str,
        sign_requests: t.Optional[
            t.Iterable[t.Union[SignRequestTemplate, t.Mapping[str, t.Any]]]
        ] = None,
    ) -> t.Iterator[PrivateCreds]:
        return self.create_host(name, typ="server", sign_requests=sign_requests)

    def create_all(self) -> None:
        for user in self.catalog.get_hosts_list():
            for _ in self.create_host(
                name=user.name, typ=user.typ, sign_requests=user.sign_requests
            ):
                continue

    def sign_all(self) -> None:
        for user in self.catalog.get_hosts_list():
            for _ in self.sign_host(name=user.name, typ=user.typ):
                continue


DEFAULT_CA_OPTIONS = CAOptions(
    name="quara",
    ips=["10.100.0.0/16"],
    duration="25950h",
    groups=[
        "users",
        "servers",
        "admin",
        "quara",
        "web",
        "rgpi",
        "kautex",
        "raynet",
        "external",
    ],
)
