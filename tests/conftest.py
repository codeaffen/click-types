"""Provide some base configurations for tests."""
import os
import pytest
import py.path  # pyright: reportMissingModuleSource=false

from ansible.errors import AnsibleError
from ansible_vault import Vault

TEST_CASES_PATH = py.path.local(__file__).realpath() / '..' / 'test_cases'


def find_all_test_cases():
    """Generate list of test cases.

    :yield: generates each test case as list item
    :rtype: str
    """
    for c in TEST_CASES_PATH.listdir(sort=True):
        c = c.basename
        if c.endswith('.py'):
            yield c.replace('.py', '')


TEST_CASES = list(find_all_test_cases())


def pytest_addoption(parser):
    """Change command line options defaults.

    We want run our tests only in three modes
    `live` - interact with an existing API
    `record` - interact with an existing API and record the interactions
    `replay` - replay previouly recorded interactions with API

    :param parser: A parser object
    :type parser: object parser
    """
    parser.addoption(
        "--vcrmode",
        action="store",
        default="replay",
        choices=["replay", "record", "live"],
        help="mode for vcr recording; one of ['replay', 'record', 'live']",
    )


@pytest.fixture
def vcrmode(request):
    """Return vcrmode of a request.

    :param request: A request object
    :type request: object request
    :return: vcrmode
    :rtype: str
    """
    return request.config.getoption("vcrmode")


def cassette_name(test_name=None):
    """Generate cassette_name."""
    return 'tests/fixtures/{0}.yml'.format(test_name)


def open_vault(vault: str = None, secret: str = None):
    s = os.getenv(secret)
    v = Vault(s)

    try:
        return dict(v.load(open(vault).read()))
    except (AnsibleError, Exception) as e:
        raise Exception(f"failed to open vault '{vault}': {str(e)}")


def get_value_from_key(data: dict = None, keys: list = None):

    if keys:

        key = keys[0]

        if isinstance(key, str) and len(keys) > 1:
            if key in data:
                return get_value_from_key(data[key], keys[1:])
            else:
                raise Exception(f"key '{key}' not in dictionary")
        elif isinstance(key, str):
            return data[key]
