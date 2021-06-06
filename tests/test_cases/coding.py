import click

from click.testing import CliRunner
from click_types.coding import SemVerParamType

semver = SemVerParamType()
runner = CliRunner()


@click.command()
@click.option('--version', type=semver)
def semver_wrapper(version):
    pass


def test_success():

    positive_semvers = [
        '1.2.3',
        '1.2.3-alpha',
        '1.2.3-beta+build1337'
    ]
    for s in positive_semvers:
        print(s)
        response = runner.invoke(semver_wrapper, ['--version', s])
        assert response.exit_code == 0


def test_failure():

    negative_semvers = [
        '1.2',
        '1.2.3+build1337',
        '1.2.3-alpha-build4711'
    ]

    for s in negative_semvers:
        response = runner.invoke(semver, ['--version', s])
        assert response.exit_code == 1
