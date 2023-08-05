# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['th2_cli',
 'th2_cli.cli',
 'th2_cli.templates',
 'th2_cli.templates.install',
 'th2_cli.templates.install.values',
 'th2_cli.utils',
 'th2_cli.utils.helm']

package_data = \
{'': ['*']}

install_requires = \
['avionix>=0.4.5,<0.5.0',
 'cassandra-driver>=3.25.0,<4.0.0',
 'colorama>=0.4.5,<0.5.0',
 'cryptography>=37.0.4,<38.0.0',
 'fire>=0.4.0,<0.5.0',
 'kubernetes>=24.2.0,<25.0.0',
 'requests>=2.28.1,<3.0.0',
 'simple-term-menu>=1.5.0,<2.0.0',
 'urllib3>=1.26.12,<2.0.0']

entry_points = \
{'console_scripts': ['th2 = th2_cli:cli']}

setup_kwargs = {
    'name': 'th2-cli',
    'version': '0.2.0',
    'description': '👨\u200d💻 CLI for managing th2 infrastructure in Kubernetes cluster',
    'long_description': '## Using\n\nInstall:\n\n```commandline\npip install th2-cli\n```\n\nRun:\n\n```commandline\nth2 install\n```\n\n## Development\n\n```\npoetry install\npoetry shell\n```\n\n```commandline\nth2 install\n```',
    'author': 'Nikolay Dorofeev',
    'author_email': 'dorich2000@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
