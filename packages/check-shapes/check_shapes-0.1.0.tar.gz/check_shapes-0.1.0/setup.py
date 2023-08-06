# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['check_shapes']

package_data = \
{'': ['*']}

install_requires = \
['lark>=1.1.0,<2.0.0',
 'tensorflow-probability>=0.12.0',
 'tensorflow>=2.4.0,<3.0.0']

setup_kwargs = {
    'name': 'check-shapes',
    'version': '0.1.0',
    'description': 'A library for annotating and checking the shapes of tensors.',
    'long_description': None,
    'author': 'Jesper Nielsen',
    'author_email': 'jespernielsen1982+check_shapes@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gpflow.github.io/check_shapes',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<3.11',
}


setup(**setup_kwargs)
