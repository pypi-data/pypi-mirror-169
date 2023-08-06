# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lacuscore']

package_data = \
{'': ['*']}

install_requires = \
['defang>=0.5.3,<0.6.0',
 'playwrightcapture>=1.15.5,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'ua-parser>=0.16.1,<0.17.0']

extras_require = \
{'docs': ['Sphinx>=5.2.2,<6.0.0']}

setup_kwargs = {
    'name': 'lacuscore',
    'version': '0.4.0',
    'description': 'Core of Lacus, usable as a module',
    'long_description': '# Modulable Lacus\n\nLacus, but as a simple module.\n\n## Installation\n\n```bash\npip install lacuscore\n```\n',
    'author': 'Raphaël Vinot',
    'author_email': 'raphael.vinot@circl.lu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
