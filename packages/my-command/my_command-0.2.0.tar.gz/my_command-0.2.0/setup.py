# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['my_command']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['my_command = my_command.my_command.main']}

setup_kwargs = {
    'name': 'my-command',
    'version': '0.2.0',
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
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
