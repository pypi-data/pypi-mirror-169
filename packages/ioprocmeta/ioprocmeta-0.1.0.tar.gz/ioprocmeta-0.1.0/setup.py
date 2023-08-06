# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ioprocmeta', 'ioprocmeta.oep']

package_data = \
{'': ['*']}

install_requires = \
['attr>=0.3.1,<0.4.0', 'cattrs>=1.8.0,<2.0.0']

setup_kwargs = {
    'name': 'ioprocmeta',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Benjamin Fuchs',
    'author_email': 'benjamin.fuchs@dlr.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
