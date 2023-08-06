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
    'version': '0.2.1',
    'description': 'Poetry plugin for logging in to AWS CodeArtifact.',
    'long_description': '# Poetry AWS CodeArtifact Login\nA Poetry plugin for authenticating with AWS CodeArtifact.\n\n## Requirements\n- `poetry >= 1.2.0`\nInstall using the dedicated installation script. See [here](https://python-poetry.org/docs/#installation). \n\n- `AWS CLI v2`\nSee [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for installation guide.\n\n\n## Intallation\n```\npoetry self add poetry-codeartifact-login\n```\n\n## Usage\nAWS credentials will need to be configured on the system prior to usage. Typically this is done using the `aws configure` command and/or directly modifying the configuration files. See [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for more info. They can also be set through [environment variables](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html), which will take precedence over any configuration file values.\n\nOnce credentials have been configured, you can log in to CodeArtifact:\n```\npoetry aws-login <source_name>\n```\n\nAssuming the credentials are configured properly and the identity they belong to has proper permissions, `poetry` will be configured with a short-lived authentication token that will automatically be used for installation of any packages in the authenticated source. See [here](https://python-poetry.org/docs/repositories/#private-repository-example) for more information on working with private repositories through `poetry`.\n\nIf want to log in with a profile other than the default, you can do:\n```\npoetry aws-login <source_name> --profile <profile_name>\n```\n\n## CLI Reference\n```\npoetry aws-login --help\n```\n',
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
