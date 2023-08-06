# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sloot']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sloot',
    'version': '0.1.0',
    'description': 'tools I usually use',
    'long_description': 'utilities\n',
    'author': 'Ja-sonYun',
    'author_email': 'killa30867@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
