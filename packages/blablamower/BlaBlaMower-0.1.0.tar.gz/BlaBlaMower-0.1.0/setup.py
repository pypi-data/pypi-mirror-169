# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blablamower', 'blablamower.core']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'blablamower',
    'version': '0.1.0',
    'description': '',
    'long_description': '# BlaBlaMower\n\n>This project is for respond to the BlaBlaCar technical test that they have asked me to work on.\n\nProgram for piloting mowers on a rectangular lawn surfaces\n',
    'author': 'Guillaume Renard',
    'author_email': 'renardguillaume@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
