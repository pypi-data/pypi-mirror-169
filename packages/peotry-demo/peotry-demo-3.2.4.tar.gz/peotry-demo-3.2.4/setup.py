# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['peotry_demo']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.23.2,<2.0.0', 'requests[security,socks]>=2.22.0,<2.23.0']

setup_kwargs = {
    'name': 'peotry-demo',
    'version': '3.2.4',
    'description': 'Poetry-demo',
    'long_description': 'None',
    'author': 'SiyuCh',
    'author_email': 'siyuch0308@gmail.com ',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
