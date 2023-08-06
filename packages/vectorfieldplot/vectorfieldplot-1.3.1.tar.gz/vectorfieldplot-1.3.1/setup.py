# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['vectorfieldplot']
install_requires = \
['lxml>=4.9.1,<5.0.0', 'numpy>=1.23.3,<2.0.0', 'scipy>=1.9.1,<2.0.0']

setup_kwargs = {
    'name': 'vectorfieldplot',
    'version': '1.3.1',
    'description': 'A python module for creating high-quality images of electric field lines.',
    'long_description': None,
    'author': 'CD Clark III',
    'author_email': 'clifton.clark@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
