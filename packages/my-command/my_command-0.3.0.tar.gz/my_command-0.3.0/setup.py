# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['my_command']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'my-command',
    'version': '0.3.0',
    'description': '',
    'long_description': '',
    'author': 'Romain Bourré',
    'author_email': 'romain.bourre@me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
