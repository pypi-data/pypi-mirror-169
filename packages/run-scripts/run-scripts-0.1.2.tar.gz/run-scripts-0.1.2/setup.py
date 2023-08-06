# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['run_scripts', 'run_scripts.commands']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['run = run_scripts.cli:cli']}

setup_kwargs = {
    'name': 'run-scripts',
    'version': '0.1.2',
    'description': 'A CLI for running npm-like scripts',
    'long_description': '# Run\n\n## Install\n\n```bash\npip install -U run-scripts\n```\n\n## Basic Usage\n\n```bash\nrun init [--short]\n# Creates either a runfile.yml or run.yml file in the current directory\n\nrun [script]\n# Runs the script defined in the runfile.yml or run.yml file\n```\n\n## Examples\n\n### runfile.yml\n\n```yaml\nscripts:\n    lint: "poetry run black ."\n    build: \n        - "run lint"\n        - "docker build -t image ."\n```',
    'author': 'Keksi',
    'author_email': 'contact@keksi.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/keksiqc/run-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
