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
    'version': '0.0.2',
    'description': 'A small library to compute group feature importance',
    'long_description': '# Group feature importance\n\n<p align="center">\n    <a href="https://github.com/BorealisAI/group-feature-importance/actions">\n      <img alt="CI" src="https://github.com/BorealisAI/group-feature-importance/workflows/CI/badge.svg?event=push&branch=main">\n    </a>\n    <a href="https://pypi.org/project/groufi/">\n      <img alt="Python" src="https://img.shields.io/pypi/pyversions/groufi.svg">\n    </a>\n    <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">\n      <img alt="Attribution-NonCommercial-ShareAlike 4.0 International" src="https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-lightgrey.svg">\n    </a>\n    <a href="https://codecov.io/gh/durandtibo/group-feature-importance">\n      <img alt="Codecov" src="https://codecov.io/gh/durandtibo/group-feature-importance/branch/main/graph/badge.svg?token=IRVV3WC71O">\n    </a>\n    <a href="https://github.com/psf/black">\n     <img  alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">\n    </a>\n    <br/>\n    <a href="https://twitter.com/intent/follow?screen_name=BorealisAI">\n        <img src="https://img.shields.io/twitter/follow/BorealisAI?style=social&logo=twitter" alt="follow on Twitter">\n    </a>\n    <br/>\n</p>\n\n\nThis repo contains the implementation to compute feature importance of correlated features.\n\n## Examples\n\nSome examples are available in [`examples`](examples)\n\n## Installation\n\n### Installing with `pip`\n\nThis repository is tested on Python 3.9, and Linux systems.\nIt is recommended to install in a virtual environment to keep your system in order.\nThe following command installs the latest version of the library:\n\n```shell\npip install groufi\n```\n\n### Installing from source\n\nTo install `groufi` from source, you can follow the steps below. First, you will need to\ninstall [`poetry`](https://python-poetry.org/docs/master/). `poetry` is used to manage and install the dependencies.\nIf `poetry` is already installed on your machine, you can skip this step. There are several ways to install `poetry` so\nyou can use the one that you prefer. You can check the `poetry` installation by running the following command:\n\n```shell\npoetry --version\n```\n\nThen, you can clone the git repository:\n\n```shell\ngit clone git@github.com:BorealisAI/group-feature-importance.git\n```\n\nThen, it is recommended to create a Python 3.8+ virtual environment. This step is optional so you can skip it. To create\na virtual environment, you can use the following command:\n\n```shell\nmake conda\n```\n\nIt automatically creates a conda virtual environment. When the virtual environment is created, you can activate it with\nthe following command:\n\n```shell\nconda activate groufi\n```\n\nThis example uses `conda` to create a virtual environment, but you can use other tools or configurations. Then, you\nshould install the required package to use `groufi` with the following command:\n\n```shell\nmake install\n```\n\nThis command will install all the required packages. You can also use this command to update the required packages. This\ncommand will check if there is a more recent package available and will install it. Finally, you can test the\ninstallation with the following command:\n\n```shell\nmake test\n```\n\n## License\n\nThis repository is released under the Attribution-NonCommercial-ShareAlike 4.0 International license as found in\nthe [LICENSE](LICENSE) file.\n',
    'author': 'Borealis AI',
    'author_email': 'None',
    'maintainer': 'Thibaut Durand',
    'maintainer_email': 'durand.tibo+gh@gmail.com',
    'url': 'https://github.com/BorealisAI/group-feature-importance',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
