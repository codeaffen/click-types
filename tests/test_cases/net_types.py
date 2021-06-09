import click
import pytest

from click.testing import CliRunner
from click_types.net import CIDRParamType, VlanIDParamType

cidr = CIDRParamType()
vlan = VlanIDParamType()
runner = CliRunner()


@click.command()
@click.option('--cidr', type=cidr)
def cidr_wrapper(cidr):
    pass


@click.command()
@click.option('--vlan', type=vlan)
def vlan_wrapper(vlan):
    pass


@pytest.mark.parametrize('param', ['192.0.2.0/24', '2001:db8::/32'])
def test_cidr_success(param):

    response = runner.invoke(cidr_wrapper, ['--cidr', param])
    print(response.output)
    assert response.exit_code == 0


@pytest.mark.parametrize('param', ['192.0.2.0', 'fe80::250/56'])
def test_cidr_failure(param):

    response = runner.invoke(cidr_wrapper, ['--cidr', param])
    print(response.output)
    assert response.exit_code != 0


@pytest.mark.parametrize('param', ['1', '1234', '4094'])
def test_vlan_success(param):

    response = runner.invoke(vlan_wrapper, ['--vlan', param])
    print(response.stdout)
    assert response.exit_code == 0


@pytest.mark.parametrize('param', ['0', '4095', -1, 0.1, 'ABCD'])
def test_vlan_failure(param):

    response = runner.invoke(vlan_wrapper, ['--vlan', param])
    print(response.output)
    assert response.exit_code != 0
