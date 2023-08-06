# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['speech_patho_mdl',
 'speech_patho_mdl.bp',
 'speech_patho_mdl.dmo',
 'speech_patho_mdl.dto',
 'speech_patho_mdl.svc']

package_data = \
{'': ['*']}

install_requires = \
['baseblock',
 'boto3',
 'openai-helper',
 'openai>=0.20.0,<0.21.0',
 'opensearch-helper',
 'opensearch-py>=1.1.0,<2.0.0',
 'owl-builder',
 'owl-parser',
 'requests',
 'schema-classification']

setup_kwargs = {
    'name': 'speech-patho-mdl',
    'version': '0.1.1',
    'description': 'Custom Trained Models for Speech Pathology',
    'long_description': None,
    'author': 'Craig Trim',
    'author_email': 'craigtrim@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.8.5',
}


setup(**setup_kwargs)
