# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neuronest', 'neuronest.core']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.3,<2.0.0',
 'opencv-contrib-python>=4.6.0.66,<5.0.0.0',
 'opencv-python-headless>=4.6.0.66,<5.0.0.0',
 'opencv-python>=4.6.0.66,<5.0.0.0']

setup_kwargs = {
    'name': 'neuronest',
    'version': '0.1.0',
    'description': 'Neuronest core project',
    'long_description': 'None',
    'author': 'Côme Arvis',
    'author_email': 'come.arvis@neuronest.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
