# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starknet_interface_generator']

package_data = \
{'': ['*']}

install_requires = \
['cairo-lang>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['starknet-interface-generator = '
                     'starknet_interface_generator.cli:main']}

setup_kwargs = {
    'name': 'starknet-interface-generator',
    'version': '0.1.0',
    'description': 'Generate interfaces for your Starknet contracts',
    'long_description': '# Cairo interface generator\n\nGenerate the interfaces corresponding to your Cairo contracts\n\n## Dependencies\n- cairo-lang\n\n## Installation\n`pip install starknet-interface-generator`\n\n## Usage\n```starknet-interface-generator file_path [-d output_directory] [-o filename]```\n\n\n## Example\n`i_main` inside the interfaces directory was generated with this command : \n```\nstarknet-interface-generator test/main-cairo -d interfaces -o i_main\n```',
    'author': 'msaug',
    'author_email': 'msaug@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
