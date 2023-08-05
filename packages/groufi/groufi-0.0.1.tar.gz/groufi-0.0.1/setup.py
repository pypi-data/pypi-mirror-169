# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['groufi']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.22.2,<2.0.0', 'pandas>=1.0.0,<2.0.0', 'scikit-learn>=1.0.0,<2.0.0']

setup_kwargs = {
    'name': 'groufi',
    'version': '0.0.1',
    'description': 'A small library to compute group feature importance',
    'long_description': '# Group feature importance\n\nThis repo contains the implementation to compute feature importance of correlated features.\n\n## Installation\n\n### Installing with `pip`\n\nTODO\n\n### Installing from source\n\nTo install `groufi` from source, you can follow the steps below. First, you will need to\ninstall [`poetry`](https://python-poetry.org/docs/master/). `poetry` is used to manage and install the dependencies.\nIf `poetry` is already installed on your machine, you can skip this step. There are several ways to install `poetry` so\nyou can use the one that you prefer. You can check the `poetry` installation by running the following command:\n\n```shell\npoetry --version\n```\n\nThen, you can clone the git repository:\n\n```shell\ngit clone git@github.com:BorealisAI/group-feature-importance.git\n```\n\nThen, it is recommended to create a Python 3.8+ virtual environment. This step is optional so you can skip it. To create\na virtual environment, you can use the following command:\n\n```shell\nmake conda\n```\n\nIt automatically creates a conda virtual environment. When the virtual environment is created, you can activate it with\nthe following command:\n\n```shell\nconda activate groufi\n```\n\nThis example uses `conda` to create a virtual environment, but you can use other tools or configurations. Then, you\nshould install the required package to use `groufi` with the following command:\n\n```shell\nmake install\n```\n\nThis command will install all the required packages. You can also use this command to update the required packages. This\ncommand will check if there is a more recent package available and will install it. Finally, you can test the\ninstallation with the following command:\n\n```shell\nmake test\n```\n',
    'author': 'Borealis AI',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/BorealisAI/group-feature-importance',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
