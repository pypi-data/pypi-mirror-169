# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kubeseal_auto']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0',
 'click>=8.1.2,<9.0.0',
 'colorama>=0.4.4,<0.5.0',
 'icecream>=2.1.2,<3.0.0',
 'kubernetes>=23.3.0,<24.0.0',
 'questionary>=1.10.0,<2.0.0',
 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['kubeseal-auto = kubeseal_auto.cli:cli']}

setup_kwargs = {
    'name': 'kubeseal-auto',
    'version': '0.4.5',
    'description': 'An interactive wrapper for kubeseal binary',
    'long_description': '<div align="center">\n\n# kubeseal-auto\n\n<b>kubeseal-auto</b> is an interactive wrapper for kubeseal binary used to encrypt secrets for [sealed-secrets](https://github.com/bitnami-labs/sealed-secrets).\n\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/shini4i/kubeseal-auto/Python%20package?style=plastic)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kubeseal-auto?style=plastic)\n![PyPI](https://img.shields.io/pypi/v/kubeseal-auto?style=plastic)\n![license](https://img.shields.io/github/license/shini4i/kubeseal-auto?style=plastic)\n\n<img src="https://raw.githubusercontent.com/shini4i/assets/main/src/kubeseal-auto/demo.gif" alt="Showcase" width="620" height="441">\n\n</div>\n\n## Installation\nThe recommended way to install this script is [pipx](https://github.com/pypa/pipx):\n\n```bash\npipx install kubeseal-auto\n```\n\n## Usage\nBy default, the script will check the version of sealed-secret controller and download the corresponding kubeseal binary to ~/bin directory.\n\nTo run the script in fully interactive mode:\n```bash\nkubeseal-auto\n```\n\nAdditionally, a "detached" mode is supported:\n```bash\n# Download sealed-secrets certificate for local signing\nkubeseal-auto --fetch\n# Generate SealedSecret with local certificate\nkubeseal-auto --cert <kubectl-context>-kubeseal-cert.crt\n```\n> Note: In the detached mode kubeseal-auto will not download the kubeseal binary and will look for it in the system $PATH.\n\nTo select kubeconfig context:\n```bash\nkubeseal-auto --select\n```\n\nTo append or change key values in the existing secret:\n```bash\nkubeseal-auto --edit secret-name.yaml\n```\n\nTo reencrypt all secrets in a directory (not working in a detached mode):\n```bash\nkubeseal-auto --reencrypt /path/to/directory\n```\n\nTo back up the encryption and decryption keys (not working in a detached mode):\n```bash\nkubeseal-auto --backup\n```\n\n## Contributing\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n',
    'author': 'Vadim Gedz',
    'author_email': 'vadims@linux-tech.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shini4i/kubeseal-auto',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
