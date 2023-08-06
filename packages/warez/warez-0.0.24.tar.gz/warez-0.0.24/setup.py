# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['warez', 'warez.pkg', 'warez.pkg.licensing', 'warez.src']

package_data = \
{'': ['*']}

install_requires = \
['clicks>=0.0.61,<0.0.62', 'pendulum>=2.1.2,<3.0.0', 'radon>=5.1.0,<6.0.0']

entry_points = \
{'console_scripts': ['warez = warez.__main__:main']}

setup_kwargs = {
    'name': 'warez',
    'version': '0.0.24',
    'description': 'tools for decentralized software development',
    'long_description': None,
    'author': 'Angelo Gladding',
    'author_email': 'angelo@ragt.ag',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
