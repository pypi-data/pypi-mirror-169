# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_codeartifact_login']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.82,<2.0.0', 'poetry>=1.2.1,<2.0.0']

entry_points = \
{'poetry.application.plugin': ['login-command = '
                               'poetry_codeartifact_login.plugin:CodeArtifactPlugin']}

setup_kwargs = {
    'name': 'poetry-codeartifact-login',
    'version': '0.1.0',
    'description': 'Poetry plugin for logging in to AWS CodeArtifact.',
    'long_description': '# Poetry AWS CodeArtifact Login\nA Poetry plugin for authenticating with AWS CodeArtifact.\n',
    'author': 'Translucence Biosystems',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
