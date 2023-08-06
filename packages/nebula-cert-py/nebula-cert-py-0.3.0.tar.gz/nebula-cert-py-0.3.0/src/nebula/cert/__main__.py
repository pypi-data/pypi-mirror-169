import json
import sys
import typing as t
from dataclasses import asdict
from pathlib import Path

import click

from nebula.cert.ca import (
    CA,
    Certificate,
    Host,
    KeyPair,
    PrivateKey,
    PublicKey,
    SignRequestTemplate,
)


@click.group()
@click.version_option(version="0.3.0")
def cli() -> None:
    pass


@click.command()
@click.option(
    "--key-file",
    "-k",
    default="~/.nebula/node.key",
    help="File where private key should be written",
)
@click.option(
    "--pub-file",
    "-p",
    default="~/.nebula/node.pub",
    help="File where public key should be written",
)
@click.option(
    "--force",
    "-f",
    is_flag=True,
    default=False,
    help="Overwrite existing files",
)
def keygen(key_file: str, pub_file: str, force: bool) -> None:
    """Generate an ED25519 private key with its associated public key"""
    keypair = CA.create_keypair()
    # Write pub
    pubout = Path(pub_file).expanduser()
    if pubout.exists():
        if not force:
            print(f"File already exists: {pubout.resolve(True).as_posix()}")
            sys.exit(1)
    pubroot = pubout.parent
    pubroot.mkdir(exist_ok=True, parents=True)
    pubout.write_bytes(keypair.public_key.as_bytes())
    # Write key
    keyout = Path(key_file).expanduser()
    keyroot = keyout.parent
    keyroot.mkdir(exist_ok=True, parents=True)
    keyout.write_bytes(keypair.private_key.as_bytes())
    # Leave a message
    print(f"Public key written to: {str(pubout)}")
    print(f"Private key written to: {str(keyout)}")
    sys.exit(0)


@click.command
def show_env() -> None:
    """Show files found within environment"""
    home = Path("~/.nebula").expanduser()
    config = home / "config.json"
    crt = home / "node.crt"
    key = home / "node.key"
    pub = home / "node.pub"
    print(
        json.dumps(
            {
                "home": home.as_posix(),
                "config": config.as_posix() if config.exists() else "",
                "certificate": crt.as_posix() if crt.exists() else "",
                "private_key": key.as_posix() if key.exists() else "",
                "public_key": pub.as_posix() if pub.exists() else "",
            },
            indent=2,
        )
    )


@click.command
def show_key() -> None:
    """Show public key"""
    try:
        host = Host.from_files()
    except FileNotFoundError:
        print("ERROR: Missing configuration in ~/.nebula/config.json")
        sys.exit(1)
    if host.public_key:
        if host.public_key._value.endswith("\n"):
            print(host.public_key, end="")
        else:
            print(host.public_key)
        sys.exit(0)
    else:
        print("ERROR: No public key", file=sys.stderr)
        sys.exit(1)


@click.command
def show_private_key() -> None:
    """Show private key"""
    try:
        host = Host.from_files()
    except FileNotFoundError:
        print("ERROR: Missing configuration in ~/.nebula/config.json")
        sys.exit(1)
    if host.private_key:
        if host.private_key._value.endswith("\n"):
            print(host.private_key, end="")
        else:
            print(host.private_key)
        sys.exit(0)
    else:
        print("ERROR: No private key", file=sys.stderr)
        sys.exit(1)


@click.command
def show_config() -> None:
    """Show user config"""
    try:
        host = Host.from_files()
    except FileNotFoundError:
        print("ERROR: Missing configuration in ~/.nebula/config.json")
        sys.exit(1)
    print(
        json.dumps(
            host.to_dict(exclude_private_key=True, exclude_public_key=True),
            indent=2,
        )
    )


@click.command
@click.option("--raw", "-r", is_flag=True, default=False)
def show_cert(raw: bool) -> None:
    """Show user certificate"""
    try:
        cert = Certificate.from_file("~/.nebula/node.crt")
    except FileNotFoundError:
        print("ERROR: No certificate found")
        sys.exit(1)
    if raw:
        cert_str = cert.as_string()
        if cert_str.endswith("\n"):
            print(cert.as_string(), end="")
        else:
            print(cert.as_string())
    else:
        print(json.dumps(asdict(cert.details), indent=2))


@click.command
@click.option("--name", "-n", help="Host name", required=True)
@click.option(
    "--typ", "--type", "-t", help="Host type ('user' or 'server')", required=True
)
@click.option("--ip", help="IP address", default=None)
@click.option("--groups", help="Groups to add", default=None)
@click.option("--subnets", help="Subnets to add", default=None)
@click.option("--duration", help="Certificate duration", default=None)
def init(
    name: str,
    typ: str,
    ip: t.Optional[str],
    groups: t.Optional[str],
    subnets: t.Optional[str],
    duration: t.Optional[str],
) -> None:
    """Init host config"""
    options = SignRequestTemplate(ip)
    try:
        keypair = KeyPair.from_values(
            PublicKey.from_file("~/.nebula/node.pub"),
            PrivateKey.from_file("~/.nebula.nod.key"),
        )
    except FileNotFoundError:
        keypair = CA.create_keypair()
    if groups:
        options.groups = groups.split(",")
    if subnets:
        options.subnets = subnets.split(",")
    if duration:
        options.duration = duration

    host = Host(
        name=name,
        typ=typ,
        public_key=keypair.public_key,
        private_key=keypair.private_key,
    )
    if ip is None:
        host.save_files()
    else:
        host.sign_requests.append(options)
        host.save_files()


@click.command
@click.option("--ip", help="IP address", default=None)
@click.option("--groups", help="Groups to add", default=None)
@click.option("--subnets", help="Subnets to add", default=None)
@click.option("--duration", help="Certificate duration", default=None)
def edit_config(
    ip: t.Optional[str],
    groups: t.Optional[str],
    subnets: t.Optional[str],
    duration: t.Optional[str],
) -> None:
    """Edit host config"""
    try:
        host = Host.from_files()
    except FileNotFoundError:
        if ip is None:
            print(
                "ERROR: No configuration to edit (file '~/.nebula/config.json' does not exist)"
            )
            sys.exit(1)
    if ip is None:
        try:
            options = host.sign_requests[0]
        except IndexError:
            print(
                "ERROR: No configuration to edit (no IP address lease found in config)"
            )
            sys.exit(1)
    else:
        options = SignRequestTemplate(ip)
    if groups:
        options.groups = groups.split(",")
    if subnets:
        options.subnets = subnets.split(",")
    if duration:
        options.duration = duration
    for idx, template in enumerate(host.sign_requests):
        if template.ip == options.ip:
            host.sign_requests[idx] = options
            break
    else:
        host.sign_requests.append(options)
    host.save_files()


@click.command
@click.option("--ca-crt", help="Path to CA certificate", default=None)
@click.option("--ca-key", help="Path to CA key", default=None)
@click.option(
    "--ca-crt-secret",
    help="Name of secret holding CA certificate within keyvault",
    default="quara-ca-cert",
)
@click.option(
    "--ca-key-secret",
    help="Name of secret holding CA certificate within keyvault",
    default="quara-ca-key",
)
@click.option(
    "--ca-keyvault",
    help="Name of keyvault holding CA certificate and key",
    default="dev-quaraneb-jqtcetl-kv",
)
@click.option("--name", help="Name of generated files", default="node")
def sign(
    ca_crt: t.Optional[str],
    ca_key: t.Optional[str],
    ca_crt_secret: str,
    ca_key_secret: str,
    ca_keyvault: str,
    name: str,
) -> None:
    """Sign a new certificate"""
    if ca_crt or ca_key:
        if not (ca_crt and ca_key):
            print("ERROR: Both --ca-crt and --ca-key must be provided when one is used")
            sys.exit(1)
        ca = CA.from_files(ca_key, ca_crt)
    else:
        ca = CA.from_keyvault(ca_keyvault, ca_crt_secret, ca_key_secret)
    try:
        host = Host.from_files()
    except FileNotFoundError:
        print("ERROR: Missing configuration in ~/.nebula/config.json")
        sys.exit(1)
    try:
        template = host.sign_requests[0]
    except IndexError:
        print("No certificate to issue")
        sys.exit(0)
    if not host.private_key:
        private_creds = ca.create_certificate(template.get_options(host.name))
        private_creds.write(name, directory="~/.nebula")
    else:
        public_creds = ca.sign_certificate(
            host.public_key, template.get_options(host.name)
        )
        public_creds.write(name, directory="~/.nebula")


cli.add_command(keygen)
cli.add_command(show_env, name="env")
cli.add_command(show_cert)
cli.add_command(show_key)
cli.add_command(show_private_key)
cli.add_command(show_config)
cli.add_command(edit_config)
cli.add_command(init)
cli.add_command(sign)


if __name__ == "__main__":
    cli()
