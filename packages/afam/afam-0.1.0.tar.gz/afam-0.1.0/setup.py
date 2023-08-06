# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['afam']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'afam',
    'version': '0.1.0',
    'description': 'ASC Files Analyzing Module',
    'long_description': '# afam - ASC Files Analyzing Module\n\nThis module allows the user to analyze a ASC file, created by the EDF2ASC translator program of\nSR Research. This program converts selected events and samples from the EyeLink EDF file into\ntext, and sorts and formats the data into a form that is easier to work with.\n\nThis module helps to perform the following operations:\n - Opening and closing the ASC file\n - Matching words and messages to keywords (tokens)\n - Reading data items from the file, including recording start, button presses, eye events and\n   messages (samples are not supported)\n\nThis module requires that `dataclasses` are available within the Python environment the user is\nrunning the module in.\n\nIt contains the following classes:\n - **ASC_BUTTON** - a dataclass used to store the data from a "BUTTON" line\n - **ASC_SBLINK** - a dataclass used to store the data from a "SBLINK" line\n - **ASC_SSACC** - a dataclass used to store the data from a "SSACC" line\n - **ASC_SFIX** - a dataclass used to store the data from a "SFIX" line\n - **ASC_EBLINK** - a dataclass used to store the data from an "EBLINK" line\n - **ASC_ESACC** - a dataclass used to store the data from an "ESACC" line\n - **ASC_EFIX** - a dataclass used to store the data from an "EFIX" line\n - **ASC_MSG** - a dataclass used to store the data from a "MSG" line\n - **ASC_File_Handler** - a class used to handle the parsing of an ASC file\n\n## Installation\n\n```bash\n$ pip install afam\n```\n\n## Usage\n\n```python\nfrom afam import ASC_File_Handler\n\nhandler = afam.ASC_File_Handler()\nevent_list = handler.read_asc_file(file_name)\n```\n\n## Contributing\n\nInterested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.\n\n## License\n\n`afam` was created by Christoph Anzengruber. It is licensed under the terms of the GNU General Public License v3.0 license.\n\n## Credits\n\n`afam` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Christoph Anzengruber',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
