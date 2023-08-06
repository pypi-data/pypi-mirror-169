# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['mzn_grader']
install_requires = \
['minizinc', 'pyyaml>=6.0,<7.0']

extras_require = \
{':python_version < "3.7"': ['dataclasses>=0.8,<0.9']}

entry_points = \
{'console_scripts': ['mzn-coursera = mzn_grader:coursera']}

setup_kwargs = {
    'name': 'mzn-grader',
    'version': '1.3.0',
    'description': 'A MOOC grading executable and library for MiniZinc modelling courses',
    'long_description': 'None',
    'author': 'Jip J. Dekker',
    'author_email': 'jip@dekker.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'py_modules': modules,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)
