# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlette_live']

package_data = \
{'': ['*'], 'starlette_live': ['statics/live/*']}

install_requires = \
['Jinja2>=3.1,<4.0', 'python-multipart>=0.0.5,<0.0.6', 'starlette>=0.20,<0.21']

setup_kwargs = {
    'name': 'starlette-live',
    'version': '0.1.0',
    'description': 'Live views for Starlette.',
    'long_description': '# OhMyAdmin\n\nAwesome admin panel for your business.\n\n![PyPI](https://img.shields.io/pypi/v/ohmyadmin)\n![GitHub Workflow Status](https://img.shields.io/github/workflow/status/alex-oleshkevich/ohmyadmin/Lint%20and%20test)\n![GitHub](https://img.shields.io/github/license/alex-oleshkevich/ohmyadmin)\n![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/ohmyadmin)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/ohmyadmin)\n![GitHub Release Date](https://img.shields.io/github/release-date/alex-oleshkevich/ohmyadmin)\n\n## Installation\n\nInstall `ohmyadmin` using PIP or poetry:\n\n```bash\npip install ohmyadmin\n# or\npoetry add ohmyadmin\n```\n\n## Features\n\n-   TODO\n\n## Quick start\n\nSee example application in `examples/` directory of this repository.\n',
    'author': 'Alex Oleshkevich',
    'author_email': 'alex.oleshkevich@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/alex-oleshkevich/starlette_live',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
