# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['quality_control']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'quality-control',
    'version': '0.0.1b0',
    'description': '',
    'long_description': '# Quality Control\n\nComing Soon\n\n',
    'author': 'Alphadelta14',
    'author_email': 'alpha@alphaservcomputing.solutions',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
