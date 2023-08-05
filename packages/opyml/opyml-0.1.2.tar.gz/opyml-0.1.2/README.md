# OPyML 🐍

> **OPML library for Python.**

## Features

* Supports all OPML versions.
* Minimal use of dependencies.
* 100% typed and tested.

## Example

```python
from opyml import OPML, Outline

# Create OPML documents from scratch.
document = OPML()
document.body.outlines.append(Outline(text="Example"))

# Convert documents to XML.
xml = document.to_xml()

# Parse OPML documents from XML.
document = OPML.from_xml(xml)
```

## Development

* Install dependencies with `poetry shell && poetry install`.
* Format code with `black opyml tests`.
* Check types with `mypy opyml`.
* Run tests and collect coverage with `pytest --cov opyml --cov-report html`.
* Generate documentation with `pdoc opyml`.

## Feedback

Found a problem or want to request a new feature? Email [helllo@holllo.org](mailto:helllo@holllo.org) and I'll see what I can do for you.

## License

Distributed under the [Apache License 2.0](https://spdx.org/licenses/Apache-2.0.html) and [MIT](https://spdx.org/licenses/MIT.html) licenses, see [LICENSE-Apache](https://git.bauke.xyz/Holllo/opyml/src/branch/main/LICENSE-Apache) and [LICENSE-MIT](https://git.bauke.xyz/Holllo/opyml/src/branch/main/LICENSE-MIT) for more information.
