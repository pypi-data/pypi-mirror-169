# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wrapper_api']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.1,<3.0.0', 'twine>=4.0.1,<5.0.0']

entry_points = \
{'console_scripts': ['realpython = reader.__main__:main']}

setup_kwargs = {
    'name': 'simple-wrapper-api',
    'version': '0.1.2',
    'description': 'Simple wrapper for APIs',
    'long_description': '',
    'author': 'pont-valabre',
    'author_email': 'dev@valabre.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.valabre.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
