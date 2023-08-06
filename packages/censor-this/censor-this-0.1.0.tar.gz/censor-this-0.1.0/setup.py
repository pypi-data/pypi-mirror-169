# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['censor_this']

package_data = \
{'': ['*']}

install_requires = \
['opencv-python>=4.6.0.66,<5.0.0.0',
 'pytesseract>=0.3.10,<0.4.0',
 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['censor-this = censor_this.main:app']}

setup_kwargs = {
    'name': 'censor-this',
    'version': '0.1.0',
    'description': 'A command line tool to censor words in an image.',
    'long_description': '# Censor It',
    'author': 'Colbe Roberson',
    'author_email': 'cgr28@njit.edu',
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
