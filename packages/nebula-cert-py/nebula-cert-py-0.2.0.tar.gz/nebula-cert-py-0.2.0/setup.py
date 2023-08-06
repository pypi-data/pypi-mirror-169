# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nebula', 'nebula.cert', 'nebula.oidc']

package_data = \
{'': ['*']}

install_requires = \
['azure-identity==1.7.1',
 'azure-keyvault-secrets==4.6.0',
 'click',
 'httpx',
 'jwt',
 'pydantic',
 'python-dateutil',
 'uvicorn']

entry_points = \
{'console_scripts': ['pync = nebula.cert.__main__:cli']}

setup_kwargs = {
    'name': 'nebula-cert-py',
    'version': '0.2.0',
    'description': 'Manage nebula certificates from Python',
    'long_description': '# Nebula Cert Python\n\n> Manager nebula certificates from Python\n\n## Prerequisite\n\nThis library expects the `nebula-cert` to be installed on host system.\n\nYou can download [latest binaries from github](https://github.com/slackhq/nebula/releases/latest):\n  - [Windows (amd64)](https://github.com/slackhq/nebula/releases/download/v1.6.1/nebula-windows-amd64.zip)\n  - [Linux (amd64)](https://github.com/slackhq/nebula/releases/download/v1.6.1/nebula-linux-amd64.tar.gz)\n  - [Linux (arm64)](https://github.com/slackhq/nebula/releases/download/v1.6.1/nebula-linux-arm64.tar.gz)\n  - [Linux (armv7)](https://github.com/slackhq/nebula/releases/download/v1.6.1/nebula-linux-arm-7.tar.gz)\n\n## Quick start\n\nRun `python -m nebula.cert` or `pync` to get started.\n\nIf you want to generate a new configuration, run `pync init --typ user --name <username>`.\n\n### Display files used by `pync`\n\n```bash\npync env\n```\n\n### Issuing certificate\n\nCheck if a config already exist:\n\n```bash\npync show-config\n```\n\nCreate a new signing request if no IP is shown:\n\n```bash\npync edit-config --ip 10.100.100.255/16 --groups "users,quara"\n```\n\nSign a new certificate\n\n```bash\npync sign\n```\n\nCheck that files were created successfully:\n\n```bash\npync env\n```',
    'author': 'charbonnierg',
    'author_email': 'guillaume.charbonnier@araymond.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
