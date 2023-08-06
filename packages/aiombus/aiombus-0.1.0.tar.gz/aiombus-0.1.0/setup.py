# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aiombus', 'aiombus.data', 'aiombus.data.block', 'aiombus.frame']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiombus',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'Sunke Schlüters',
    'author_email': 'post@scus.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
