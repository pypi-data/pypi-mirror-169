# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['wotw']

package_data = \
{'': ['*']}

modules = \
['py']
setup_kwargs = {
    'name': 'wotw',
    'version': '0.1.0',
    'description': 'Watcher On The Wall watches directories for changes',
    'long_description': '# wotw - The Watcher On The Wall\n\nCapture the name edition - Not For Use.\n',
    'author': 'Simon Kennedy',
    'author_email': 'sffjunkie+code@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'py_modules': modules,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
