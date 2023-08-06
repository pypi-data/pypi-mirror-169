# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['legendkit']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5,<4.0', 'pandas>=1.4.4,<2.0.0', 'scipy>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'legendkit',
    'version': '0.2.0',
    'description': 'Legend creation and manipulation with ease for matplotlib',
    'long_description': '<p align="center">\n<img src="https://raw.githubusercontent.com/Mr-Milk/legendkit/main/images/legendkit-project.svg">\n</p>\n\n![pypi version](https://img.shields.io/pypi/v/legendkit?color=blue&logo=python&logoColor=white&style=flat-square)\n\nWhen you want to create or adjust the legend in matplotlib, things can get dirty. \nLegendKit may solve your headache.\n\n<img src="https://raw.githubusercontent.com/Mr-Milk/legendkit/main/images/showcase.svg">\n\n## Features\n\n- Easy title placement and alignment\n- Layout for multiple legends\n- Easy colorbar\n\n## Installation\n\n```shell\npip install legendkit\n```\n',
    'author': 'Mr-Milk',
    'author_email': 'yb97643@um.edu.mo',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Mr-Milk/legendkit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
