# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['scikit_talk']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.0,<2.0.0']

entry_points = \
{'console_scripts': ['scikit_talk_prepocessor = '
                     'my_package.preprocessor:cha_to_dataframe']}

setup_kwargs = {
    'name': 'scikit-talk',
    'version': '0.0.251',
    'description': 'A Python package to help you process real world conversation speech data.',
    'long_description': '',
    'author': 'Andreas Liesenfeld',
    'author_email': 'None',
    'maintainer': 'Andreas Liesenfeld',
    'maintainer_email': 'None',
    'url': 'https://python-poetry.org/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
