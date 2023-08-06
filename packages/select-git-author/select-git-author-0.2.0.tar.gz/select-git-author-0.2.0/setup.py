# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['select_git_author']

package_data = \
{'': ['*']}

install_requires = \
['click-prompt>=0.5.1,<0.6.0']

entry_points = \
{'console_scripts': ['commit = select_git_author.cli:cli']}

setup_kwargs = {
    'name': 'select-git-author',
    'version': '0.2.0',
    'description': 'Interactively select the author for the next git commit',
    'long_description': None,
    'author': 'Markus Grotz',
    'author_email': 'markus.grotz@kit.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.9,<4.0',
}


setup(**setup_kwargs)
