# click-types: Python library that provides useful click types

[![PyPI version](https://badge.fury.io/py/click-types.svg)](https://badge.fury.io/py/click-types)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ed3511c33a254bfe942777c9ef3251e3)](https://www.codacy.com/gh/codeaffen/click-types/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=codeaffen/click-types&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/click-types/badge/?version=develop)](https://click-types.readthedocs.io/en/develop/?badge=develop)

[click](https://click.palletsprojects.com) is the `Command line interface creation kit` and it helps you to create command line interfaces with some few lines of code. Click comes with meaningful defauls to make starting with it as easy as possible.

A powerful feature of click is to develop custom types to convert and/or validate user input. There are several custom types in the wild but this repository is intended to collect such custom types to make it easily accessable.

## Installation

Currently we support two ways of installing `click-types` on your system. We will both illustrate short in the following sections.

### Installing from pypi

We release all versions on [pypi.org](https://pypi.org/project/click-types/), so you can simply use `pip` to install it.

~~~bash
pip install click-types
~~~

### Install from repository

Alternatively you can install it from a local clone of our [github repository](https://github.com/codeaffen/click-types).

~~~bash
$ git clone https://github.com/codeaffen/click-types.git
Cloning into 'click-types'...
remote: Enumerating objects: 83, done.
remote: Counting objects: 100% (83/83), done.
remote: Compressing objects: 100% (59/59), done.
remote: Total 83 (delta 25), reused 72 (delta 16), pack-reused 0
Unpacking objects: 100% (83/83), 29.77 KiB | 441.00 KiB/s, done.
$ cd click-types/
$ python setup.py install
~~~

## Custom types

Name | Module | Description
---- | ------ | -----------
AnsibleVaultParamType | click_type.ansible | Manages secret values in ansible vaults. This type open the configured vault put the value to the given path and close vault.
SemVerParamType | click_types.coding | Provides validity checks for semantic versions.
CIDRParamType | click_types.net | Checking a given IP network/prefix if it's a valid CIDR. Both ip version (v4 and v6) are supported.
VlanParamType | click_types.net | Validates vlan ids according to IEEE 802.1Q standard.
