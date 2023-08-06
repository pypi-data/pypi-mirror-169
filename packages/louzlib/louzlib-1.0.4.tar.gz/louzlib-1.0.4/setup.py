# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['louzlib', 'louzlib.env', 'louzlib.log', 'louzlib.owl', 'louzlib.sty']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'fontawesome>=5.10.1.post1,<6.0.0',
 'lxml>=4.9.1,<5.0.0',
 'pandas>=1.4.4,<2.0.0',
 'ptpython>=3.0.20,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'randomname>=0.1.5,<0.2.0',
 'requests>=2.28.1,<3.0.0',
 'typer>=0.6.1,<0.7.0']

setup_kwargs = {
    'name': 'louzlib',
    'version': '1.0.4',
    'description': 'like xanax but for the python.',
    'long_description': '# xanax\n',
    'author': 'lmisto',
    'author_email': 'louaimisto@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'http://github.com/lmist/louzlib',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
