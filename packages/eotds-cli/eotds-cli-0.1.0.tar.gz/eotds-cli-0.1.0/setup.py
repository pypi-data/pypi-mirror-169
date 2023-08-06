# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['eotds_cli']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.1.0,<0.2.0']

entry_points = \
{'console_scripts': ['eotds-cli = eotds_cli.main:app']}

setup_kwargs = {
    'name': 'eotds-cli',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Juan Sensio',
    'author_email': 'it@earthpulse.es',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
