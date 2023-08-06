# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scikit_talk']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'scikit-talk',
    'version': '0.0.250',
    'description': 'A Python package to help you process real world conversation speech data.',
    'long_description': '',
    'author': 'Gábor Parti',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
