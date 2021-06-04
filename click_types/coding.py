"""Module for custom click types regarding to development."""

import semver

from click import ParamType


class SemVerParamType(ParamType):
    """Provide a custom click type for semantic versions.

    This custom click type provides validity checks for semantic versions.
    """
    name = 'semver'

    def convert(self, value, param, ctx):
        """Converts the value from string into semver type.

        This method takes a string and check if this string belongs to semantic verstion definition.
        If the test is passed the value will be returned. If not a error message will be prompted.

        :param value: the value passed
        :type value: str
        :param param: the parameter that we declared
        :type param: str
        :param ctx: context of the command
        :type ctx: str
        :return: the passed value as a checked semver
        :rtype: str
        """
        try:
            semver.parse(value)
            return value
        except ValueError as e:
            self.fail('Not a valid version, {0}'.format(str(e)), param, ctx)
