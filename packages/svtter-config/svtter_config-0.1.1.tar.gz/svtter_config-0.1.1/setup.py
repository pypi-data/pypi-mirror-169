# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['svtter_config']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'svtter-config',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'svtter',
    'author_email': 'svtter@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/svtter/svtter_config',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
