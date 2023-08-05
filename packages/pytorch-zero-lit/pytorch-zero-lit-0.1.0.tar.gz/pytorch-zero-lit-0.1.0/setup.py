# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lit']

package_data = \
{'': ['*']}

install_requires = \
['onnxruntime>=1.12.1,<2.0.0',
 'pytorch-lantern>=0.12.1,<0.13.0',
 'transformers>=4.22.1,<5.0.0']

setup_kwargs = {
    'name': 'pytorch-zero-lit',
    'version': '0.1.0',
    'description': 'LiT: Zero-Shot Transfer with Locked-image text Tuning',
    'long_description': None,
    'author': 'Richard Löwenström',
    'author_email': 'samedii@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
