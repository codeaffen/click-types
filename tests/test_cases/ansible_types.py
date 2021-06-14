import click
import os
import random
import string
import tempfile

from tests.conftest import open_vault, get_value_from_key
from click.testing import CliRunner
from click_types.ansible import AnsibleVaultParamType as vault


sec_env = 'TEST_VAULT_PASSPHRASE'
key_path = 'key.subkey.subsubkey'
vault_file = tempfile.NamedTemporaryFile().name
os.environ[sec_env] = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))

runner = CliRunner()


@click.command()
def vault_wrapper():
    click.prompt('value please', type=vault(vault_file, sec_env, key_path))


def test_create_value():
    value = 'initial value'
    response = runner.invoke(vault_wrapper, input=value)

    decrypted_data = open_vault(vault_file, sec_env)

    assert response.exit_code == 0
    assert get_value_from_key(decrypted_data, key_path.split('.')) == value


def test_update_value():
    value = 'updated value'
    response = runner.invoke(vault_wrapper, input=value)

    decrypted_data = open_vault(vault_file, sec_env)

    assert response.exit_code == 0
    assert get_value_from_key(decrypted_data, key_path.split('.')) == value


def test_missing_env_var():
    del os.environ[sec_env]
    response = runner.invoke(vault_wrapper, input='dummy')

    assert response.exit_code != 0
