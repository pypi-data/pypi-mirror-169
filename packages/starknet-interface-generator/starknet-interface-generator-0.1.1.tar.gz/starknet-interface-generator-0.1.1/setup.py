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
    'version': '0.1.1',
    'description': 'Generate interfaces for your Starknet contracts',
    'long_description': '# Starknet interface generator\n\nGenerate the interfaces corresponding to your Starknet contracts.\n\n## Dependencies\n\n- cairo-lang\n\n## Installation\n\n`pip install starknet-interface-generator`\n\n## Usage\n\n`starknet-interface-generator file_path [-d output_directory] [-o filename]`\n\n## Example\n\n`i_main` inside the interfaces directory was generated with this command :\n\n```\nstarknet-interface-generator test/main-cairo -d interfaces\n```\n\n## Protostar\n\nYou can use starknet-interface-generator in a protostar project.\nThis can be paired with a github action to automatically generate the interfaces for the contracts\nthat specified inside the `protostar.toml` file.\n\n`starknet-interface-generator --protostar`\n',
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
