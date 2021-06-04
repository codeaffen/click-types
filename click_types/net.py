"""Module for custom click types regarding to network."""

import click
import ipaddress
import re


class CIDRParamType(click.ParamType):
    """Provide a custom click type for network cidr handling.

    This custom click type provides validity check for network cidrs.
    Both ip version (v4 and v6) are supported.
    """
    name = "cidr"

    def convert(self, value, param, ctx):
        """Converts the value from string into cidr type.

        This method takes a string and check if this string belongs to ipv4 or ipv6 cidr definition.
        If the test is passed the value will be returned. If not a error message will be prompted.

        :param value: the value passed
        :type value: str
        :param param: the parameter that we declared
        :type param: str
        :param ctx: context of the command
        :type ctx: str
        :return: the passed value as a checked cidr
        :rtype: int
        """
        try:
            if "/" in value:
                if "." in value and ":" not in value:
                    ipaddress.IPv4Network(value)
                elif ":" in value and "." not in value:
                    ipaddress.IPv6Network(value)
            else:
                raise ValueError('{0} has not bit mask set'.format(value))
        except (ValueError, ipaddress.AddressValueError) as e:
            self.fail('Not a network cidr, {0}'.format(str(e)), param, ctx)

        return value


class VlanIDParamType(click.ParamType):
    """Provide a custom click type for vlan id handling.

    This custom click type provides validity checks for vlan ids according to IEEE 802.1Q standard.
    """
    name = 'vlanid'

    def convert(self, value, param, ctx):
        """Converts the value from string into semver type.

        This method tages a string and check if this string belongs to semantic verstion definition.
        If the test is passed the value will be returned. If not a error message will be prompted.

        :param value: the value passed
        :type value: str
        :param param: the parameter that we declared
        :type param: str
        :param ctx: context of the command
        :type ctx: str
        :return: the passed value as a checked vlan id
        :rtype: int
        """
        try:
            if re.match(r'^[\d]{1,4}$', value):
                if 1 <= int(value) <= 4094:
                    return int(value)
                else:
                    raise ValueError('{0} is not within valid vlan id range'.format(value))
            else:
                raise ValueError('{0} is not match vlan id pattern'.format(value))
        except ValueError as e:
            self.fail('Not a valid vlan id, {0}'.format(str(e)), param, ctx)
