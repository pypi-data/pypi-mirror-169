# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kandji']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'kandji',
    'version': '0.1.0',
    'description': 'A python wrapper for the Kandji API',
    'long_description': None,
    'author': 'Fredrik Haarstad',
    'author_email': 'codemonkey@zomg.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/frefrik/python-kandji',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
