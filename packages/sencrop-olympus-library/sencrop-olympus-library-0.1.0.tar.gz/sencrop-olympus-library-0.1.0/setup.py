# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['sencrop_olympus_library', 'sencrop_olympus_library.metrics']

package_data = \
{'': ['*']}

install_requires = \
['pre-commit>=2.20.0,<3.0.0']

setup_kwargs = {
    'name': 'sencrop-olympus-library',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
