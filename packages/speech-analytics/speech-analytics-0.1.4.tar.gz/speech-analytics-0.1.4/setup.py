# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['speech_analytics']

package_data = \
{'': ['*']}

install_requires = \
['spacy>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'speech-analytics',
    'version': '0.1.4',
    'description': '',
    'long_description': '',
    'author': 'Ashleigh Richardson',
    'author_email': 'ashleigh.richardson@uqconnect.edu.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
