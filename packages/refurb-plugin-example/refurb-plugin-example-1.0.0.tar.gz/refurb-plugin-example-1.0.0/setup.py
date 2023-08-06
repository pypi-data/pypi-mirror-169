# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['refurb_plugin_example']

package_data = \
{'': ['*']}

install_requires = \
['refurb==0.2.4']

entry_points = \
{'refurb.plugins': ['module = refurb_plugin_example']}

setup_kwargs = {
    'name': 'refurb-plugin-example',
    'version': '1.0.0',
    'description': 'An example plugin for Refurb',
    'long_description': '# Refurb Plugin Example\n\nThis repo is meant to be a good starting point for those who are looking to\nmake plugins for Refurb.\n\nFor illustrative purposes, this plugin will emit an error when the following\n`print` statement is found:\n\n```python\nprint("Hello world!")\n```\n\n## Setup\n\nFirst things first, fork this repo. Make sure to change the name, but keep\nthe `refurb-` prefix (for naming convention sake).\n\nNext, clone:\n\n```\n$ git clone https://github.com/USERNAME/refurb-your-plugin\n$ cd refurb-your-plugin\n```\n\nOf course, replacing `refurb-your-plugin` with the name you picked.\n\nThen, update the `pyproject.toml` file with the your information.\nYou can run the `setup.sh` script to do this for you, which will ask you a series\nof questions. If the script does not work, you will have to update it manually\n(you should only need to update the first two sections).\n\n## Check Discovery\n\nIn order for Refurb to find and use your check, 2 conditions must be met:\n\n1. You must export a class that starts with `Error`, which will contain the error metadata. Note:\n  * It must derive from `Error`\n  * It cannot be named `ErrorCode`\n2. You must have a function called `check`, which is the entry point for a given check.\n\nThe definition for a `check` function looks something like this:\n\n```\ndef check(node: CallExpr, errors: list[Error]) -> None:\n    ...\n```\n\nWhere `CallExpr` is the node you want to accept, and `errors` is where you append an\nerror if one occurs. You can accept multiple node types using a type union, like so:\n\n```\ndef check(node: UnaryExpr | OpExpr, errors: list[Error]) -> None:\n    ...\n```\n\nThis check will accept both unary and binary expressions.\n\nAny nested folders must contain an `__init__.py` file. This might not be 100% necessary,\nbut from what I can tell, it is best to add it in anyways.\n',
    'author': 'dosisod',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dosisod/refurb-plugin-example',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
