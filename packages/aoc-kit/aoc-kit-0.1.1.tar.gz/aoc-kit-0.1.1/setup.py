# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aockit']

package_data = \
{'': ['*']}

install_requires = \
['python-dotenv>=0.21.0,<0.22.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['aoc-download = aockit.download:main']}

setup_kwargs = {
    'name': 'aoc-kit',
    'version': '0.1.1',
    'description': 'Toolkit for advent of code',
    'long_description': "# Advent Of Code kit\n\nA supportive lib for advent of code challenges.\n\n\n## Getting started\n\nMake sure to add `AOC_TOKEN` to your .env file.\n(You can find the token in your cookies when browsing on advendofcode.com)\n\n## Example\n\n```\nfrom aockit import get_input\n\ndef process(data):\n    return 'implement me'\n\ndata = get_input(2015, 1)\nresult = process(data)\nprint(result)\n```\n",
    'author': 'Pierre Hoffmeister',
    'author_email': 'pierre.git@posteo.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
