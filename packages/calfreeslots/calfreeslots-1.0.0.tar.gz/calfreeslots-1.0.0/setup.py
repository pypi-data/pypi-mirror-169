# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calfreeslots']

package_data = \
{'': ['*']}

install_requires = \
['arrow>=1.2.3,<2.0.0',
 'icalendar>=4.1.0,<5.0.0',
 'recurring-ical-events>=1.0.2-beta.0,<2.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['calfreeslots = calfreeslots:main']}

setup_kwargs = {
    'name': 'calfreeslots',
    'version': '1.0.0',
    'description': 'Command line utility to print free calendar slots in the coming days.',
    'long_description': None,
    'author': 'Johannes Köster',
    'author_email': 'johannes.koester@uni-due.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
