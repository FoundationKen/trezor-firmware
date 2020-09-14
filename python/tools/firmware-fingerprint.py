#!/usr/bin/env python3

import sys
import click

from trezorlib import firmware
from trezorlib._internal import firmware_headers


@click.command()
@click.argument("filename", type=click.File("rb"))
@click.option("-o", "--output", type=click.File("w"), default="-")
def firmware_fingerprint(filename, output):
    """Display fingerprint of a firmware file."""
    data = filename.read()

    try:
        # Unsigned production builds for Trezor T do not have valid code hashes.
        # Use the internal module which recomputes them first.
        if data[:4] == b"TRZV":
            fw = firmware_headers.parse_image(data)
            fingerprint = fw.digest()
        else:
            version, fw = firmware.parse(data)
            fingerprint = firmware.digest(version, fw)
    except Exception as e:
        click.echo(e, err=True)
        sys.exit(2)

    click.echo(fingerprint.hex(), file=output)


if __name__ == "__main__":
    firmware_fingerprint()
