# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['blablamower', 'blablamower.core']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['blablamower = blablamower.__main__:main']}

setup_kwargs = {
    'name': 'blablamower',
    'version': '1.0.0',
    'description': '',
    'long_description': '# BlaBlaMower\n\n>This project is for respond to the BlaBlaCar technical test that they have asked me to work on. The specifications are on this file [*specs/BlaBlaCar_Technical Test.md*](/specs/BlaBlaCar_Technical%20Test.md)\n\nProgram for mowing a rectangular lawn surface with multiple mowers.\n\n[CHANGELOG](./CHANGELOG.md)\n\n## Installation\n\n> pip and python3.8+ is required\n\n### pypi\n```shell\n$> pip install blablamower\n```\n\n### Release\n```shell\n$> wget https://github.com/renardguill/BlaBlaMower/releases/download/v1.0.0/blablamower-1.0.0-py3-none-any.whl\n$> pip install blablamower-1.0.0-py3-none-any.whl\n```\n\n### Source code\n\n> poetry is needed\n```shell\n$> git clone https://github.com/renardguill/BlaBlaMower.git\n$> cd BlaBlaMower\n$> poetry build\n$> pip install dist/blablamower-1.0.0-py3-none-any.whl\n```\n\n## Update\n\n### pypi\n```shell\n$> pip install blablamower --upgrade\n```\n\n\n## Usage\n\nThe program expect an input file constructed in the following manner: :\n\n>The first line corresponds to the upper right corner of the lawn. The bottom left corner is\nimplicitly (0, 0).\nThe rest of the file describes the multiple mowers that are on the lawn. Each mower is described\non two lines:\nThe first line contains the mower\'s starting position and orientation in the format "X Y O". X and\nY are the coordinates and O is the orientation.\nThe second line contains the instructions for the mower to navigate the lawn. The instructions\nare not separated by spaces.\n\nexemple :\n```txt\n5 5\n1 2 N\nLFLFLFLFF\n3 3 E\nFFRFFRFRRF\n```\n\n```shell\n$> blablamower ./inputfile.txt\n```',
    'author': 'Guillaume Renard',
    'author_email': 'renardguillaume@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/renardguill/BlaBlaMower',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
