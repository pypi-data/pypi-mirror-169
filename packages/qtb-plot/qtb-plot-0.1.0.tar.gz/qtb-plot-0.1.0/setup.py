# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['qtbplot']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.6.0,<4.0.0']

setup_kwargs = {
    'name': 'qtb-plot',
    'version': '0.1.0',
    'description': 'Standard plotting styles of our institute',
    'long_description': '# QTB Plot\n\nThis package is basically just a convenience matplotlib option setter. \nYou have two ways of using it. \nWith `set_style` you set the style for the entire notebook or whatever session \nyou are working in and with `plotting_context` you create a context manager \nthat will only set the style locally for the current plot.\n\nTake a look at the supplied tutorial notebok to see how this is done.\n\n\nThe easiest way of installing the package is to cd into the package folder and to install it locally with\n`pip install -e .`\n',
    'author': 'Marvin van Aalst',
    'author_email': 'marvin.vanaalst@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://gitlab.com/marvin.vanaalst/qtb-plot',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
