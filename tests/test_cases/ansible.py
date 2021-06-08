import click
import os
import random
import string

from click.testing import CliRunner
from click_types.ansible import AnsibleVaultParamType as vault


sec_env = 'TEST_VAULT_PASSPHRASE'
key_path = 'key.subkey.subsubkey'
vault_file = '/tmp/xyz.yml'
os.environ[sec_env] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))

runner = CliRunner()


@click.command()
def vault_wrapper():
    click.prompt('value please', type=vault(vault_file, sec_env, key_path))


def test_create_value():
    response = runner.invoke(vault_wrapper, input='initial value')
    assert response.exit_code == 0


def test_update_value():
    response = runner.invoke(vault_wrapper, input='updated value')
    assert response.exit_code == 0


if __name__ == "__main__":
    vault_wrapper()
