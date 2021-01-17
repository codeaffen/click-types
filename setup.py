from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="click-types",
    version="1.0.0",
    author="Christian Meißner",
    author_email="Christian Meißner <cme@codeaffen.org>",
    description="Python library that provides useful click types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    platform="Independent",
    url="https://codeaffen.org/projects/click-types/",
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
    keywords='click types',
    python_requires='>=3.6',
    install_requires=[
        'ansible',
        'ipaddress',
        'click',
        'semver'
    ],
)
