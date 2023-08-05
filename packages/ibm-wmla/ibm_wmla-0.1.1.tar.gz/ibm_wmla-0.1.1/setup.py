# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ibm_wmla']

package_data = \
{'': ['*']}

install_requires = \
['ibm-cloud-sdk-core>=3.15.3,<4.0.0',
 'python_dateutil>=2.5.3,<3.0.0',
 'requests>=2.20,<3.0']

setup_kwargs = {
    'name': 'ibm-wmla',
    'version': '0.1.1',
    'description': 'Python client library for IBM Watson Machine Learning Accelerator',
    'long_description': 'Welcom to ``ibm-wmla``\n=======================\n\n``ibm-wmla`` is a Python library that allows to work with IBM Watson Machine Learning Accelerator.\n\n`IBM Watson Machine Learning Accelerator Inference APIs`_\n\n.. _IBM Watson Machine Learning Accelerator Inference APIs: https://www.ibm.com/docs/en/wmla/2.3?topic=workload-inference\n\n',
    'author': 'Shuang Yu',
    'author_email': 'shuang.yu@ibm.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sherryyyu/ibm-wmla-python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
