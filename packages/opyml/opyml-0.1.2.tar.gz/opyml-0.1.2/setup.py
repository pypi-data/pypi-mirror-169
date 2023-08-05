# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['opyml']

package_data = \
{'': ['*']}

install_requires = \
['defusedxml>=0.7.1,<0.8.0']

setup_kwargs = {
    'name': 'opyml',
    'version': '0.1.2',
    'description': 'OPML library for Python.',
    'long_description': '# OPyML 🐍\n\n> **OPML library for Python.**\n\n## Features\n\n* Supports all OPML versions.\n* Minimal use of dependencies.\n* 100% typed and tested.\n\n## Example\n\n```python\nfrom opyml import OPML, Outline\n\n# Create OPML documents from scratch.\ndocument = OPML()\ndocument.body.outlines.append(Outline(text="Example"))\n\n# Convert documents to XML.\nxml = document.to_xml()\n\n# Parse OPML documents from XML.\ndocument = OPML.from_xml(xml)\n```\n\n## Development\n\n* Install dependencies with `poetry shell && poetry install`.\n* Format code with `black opyml tests`.\n* Check types with `mypy opyml`.\n* Run tests and collect coverage with `pytest --cov opyml --cov-report html`.\n* Generate documentation with `pdoc opyml`.\n\n## Feedback\n\nFound a problem or want to request a new feature? Email [helllo@holllo.org](mailto:helllo@holllo.org) and I\'ll see what I can do for you.\n\n## License\n\nDistributed under the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html) and [MIT](https://spdx.org/licenses/MIT.html) licenses, see [LICENSE-Apache](https://git.bauke.xyz/Holllo/opyml/src/branch/main/LICENSE-Apache) and [LICENSE-MIT](https://git.bauke.xyz/Holllo/opyml/src/branch/main/LICENSE-MIT) for more information.\n',
    'author': 'Holllo',
    'author_email': 'helllo@holllo.cc',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://git.bauke.xyz/Holllo/opyml',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
