"""Module for custom click types regarding to ansible."""

import click
import os
import yaml

from ansible.errors import AnsibleError
from ansible_vault import Vault
from yaml import SafeLoader


class AnsibleVaultParamType(click.ParamType):
    """Provide a custom click type for ansible vaults.

    This custom click type provides managing passed values in a given vault.
      * decrypt vault
      * save passed value
      * encrypt vault
    """
    name = 'vault'

    vault = str
    secret = str
    path = str

    def __init__(self, vault: str, secret: str, path: str):
        """Create a AnsibleVaultParamType object.

        This method takes three arguments that are necessary to initialize a AnsibleVaultParamType object.

        :param vault: Path to the vault file.
        :type vault: str
        :param secret: Name of the Environement variable that stores the vault passphrase.
        :type secret: str
        :param path: Path where the passed value should be saved in dotted notation.
        :type path: str
        """
        try:
            s = os.getenv(secret)
            self.v = Vault(s)
        except (TypeError, ValueError):
            self.fail('Environment variable \'{0}\' not set.'.format(secret))

        self.vault = vault
        self.path = path

        super(AnsibleVaultParamType, self).__init__()

    def convert(self, value, param, ctx):
        """Open vault and save vaule at the given path.

        :param value: the value passed
        :type value: str
        :param param: the parameter that we declared
        :type param: str
        :param ctx: context of the command
        :type ctx: str
        :return: the passed value as a checked semver
        :rtype: str
        """
        data = {}
        try:
            if os.path.exists(self.vault):
                data = self.v.load(open(self.vault).read())
        except AnsibleError as e:
            if 'not vault encrypted data' in str(e):
                data = yaml.safe_load(open(self.vault).read(), SafeLoader) or {}
        except Exception as e:
            self.fail('Decryption failed: {0}'.format(str(e)), param, ctx)

        data = self._populate_data(data, self.path.split('.'), value)
        with open(self.vault, "w") as f:
            yaml.dump(data, f)

        try:
            self.v.dump(data, open(self.vault, 'w'))
        except Exception:
            self.fail('Error while encrypting data', param, ctx)

        return self.path

    def _populate_data(self, origin: dict = None, keys: list = None, value: str = None):
        """Save value at the desired position in vault.

        This method takes vault data, a list of keys where to store the value.

        :param origin: The dictionary of vault data, defaults to {}
        :type origin: dict, optional
        :param keys: List of keys that describe the desired position in vault, defaults to []
        :type keys: list, optional
        :param value: The value to store in vault, defaults to None
        :type value: str, optional
        :return: The vault data extended by `value` at the desired position.
        :rtype: dict
        """
        data = origin.copy()

        if keys:
            key = keys[0]

            if isinstance(key, str) and len(keys) > 1:
                if key in data:
                    data[key].update(self._populate_data({}, keys[1:], value))
                else:
                    data[key] = {}
                    data[key].update(self._populate_data({}, keys[1:], value))
            elif isinstance(key, str):
                if key in data:
                    data[key].update(self._populate_data({}, keys[1:], value))
                else:
                    data[key] = value
        return data
