# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poet_plugin']

package_data = \
{'': ['*']}

install_requires = \
['poetry>=1.2.0,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['poet_plugin = poet_plugin.plugin:PEGPlugin']}

setup_kwargs = {
    'name': 'poet-plugin',
    'version': '0.1.2',
    'description': 'A Poetry plugin to enable exclusivity between groups',
    'long_description': '# Poet Plugin\nA Poetry plugin to enable exclusivity between groups.  \nPoet stands for **Po**etry **E**xclusivity **T**oggle (or some other excuse, I did not want a verbose package name and\n`poet` seemed short and sweet since this plugin changes the internal poetry package during runtime).\n\n## Installation\nSimply add this plugin as a dependency with `pip install poet-plugin`.\n\n## Usage\nWhen running `poetry install`, the various options (`--only`, `--without`) are parsed to ensure the dependency resolver \nonly considers what needs to be considered.  \nThis allows a non-mutually exclusive group definition, so that e.g. the `dev` group can refer to\nsome local path, whereas a `prod` group refers to git URI.  \n\n### Examples\nConsidering the following `pyproject.toml`, depicting a mono-repository:\n```\n[tool.poetry.dependencies]\npython = ">=3.8,<3.12"\npoetry = "^1.2.0"\n\n[tool.poetry.group.prod.dependencies]\nfoo = {git = "https://github.com/bar/foo", subdirectory = "src/libs/foo"}\n\n[tool.poetry.group.dev.dependencies]\nfoo = {path = "../../libs/foo", develop = true}\n```\n- Install the prod version:\n  - `poetry install --without dev`, OR\n  - `poetry install --only prod`\n- Install the dev version:\n  - `poetry install --without prod`, OR\n  - `poetry install --only dev`',
    'author': 'Idan Tene',
    'author_email': 'idan.tene@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
