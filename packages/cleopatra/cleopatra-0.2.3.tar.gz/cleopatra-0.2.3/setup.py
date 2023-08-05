# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cleopatra']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.3,<4.0.0', 'numpy>=1.23.3,<2.0.0']

setup_kwargs = {
    'name': 'cleopatra',
    'version': '0.2.3',
    'description': 'visualization package',
    'long_description': 'None',
    'author': 'Mostafa Farrag',
    'author_email': 'moah.farag@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MAfarrag/cleopatra',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
