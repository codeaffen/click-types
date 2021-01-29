#!/usr/bin/env python
import click

from click_types.coding import SemVerParamType

semver = SemVerParamType()


def test_semver():
    version = click.prompt("Enter semantic version", type=semver)
    click.echo('Passed: Valid version, {0} is a valid SemVer string'.format(version))


if __name__ == "__main__":
    while True:
        test_semver()
