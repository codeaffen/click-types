import click
import pytest

from click.testing import CliRunner
from click_types.coding import SemVerParamType

semver = SemVerParamType()
runner = CliRunner()


@click.command()
@click.option('--version', type=semver)
def semver_wrapper(version):
    pass


@pytest.mark.parametrize('param', ['1.2.3', '1.2.3-alpha', '1.2.3-beta+build1337'])
def test_success(param):

    response = runner.invoke(semver_wrapper, ['--version', param])
    assert response.exit_code == 0


@pytest.mark.parametrize('param', ['1.2', '1.2.3+build1337', '1.2.3-alpha-build4711'])
def test_failure(param):

    response = runner.invoke(semver, ['--version', param])
    assert response.exit_code != 0
