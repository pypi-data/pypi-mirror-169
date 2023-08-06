# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jsonschema2md2']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.1', 'click>=7']

extras_require = \
{':python_version < "3.8"': ['importlib_metadata>=1,<2']}

entry_points = \
{'console_scripts': ['jsonschema2md = jsonschema2md2:main']}

setup_kwargs = {
    'name': 'jsonschema2md2',
    'version': '0.5.1',
    'description': 'Convert JSON Schema to human-readable Markdown documentation',
    'long_description': '# jsonschema2md\n\n[![](https://flat.badgen.net/pypi/v/jsonschema2md?icon=pypi)](https://pypi.org/project/jsonschema2md)\n[![](https://flat.badgen.net/github/release/ralfg/jsonschema2md)](https://github.com/ralfg/jsonschema2md/releases)\n[![](https://flat.badgen.net/github/checks/ralfg/jsonschema2md/)](https://github.com/ralfg/jsonschema2md/actions)\n[![](https://flat.badgen.net/codecov/c/github/ralfg/jsonschema2md)](https://codecov.io/gh/RalfG/jsonschema2md)\n![](https://flat.badgen.net/github/last-commit/ralfg/jsonschema2md)\n![](https://flat.badgen.net/github/license/ralfg/jsonschema2md)\n\n\n*Convert JSON Schemas to simple, human-readable Markdown documentation.*\n\n---\n\nFor example:\n```json\n{\n    "$id": "https://example.com/person.schema.json",\n    "$schema": "http://json-schema.org/draft-07/schema#",\n    "title": "Person",\n    "description": "JSON Schema for a person object.",\n    "type": "object",\n    "properties": {\n      "firstName": {\n        "type": "string",\n        "description": "The person\'s first name."\n      },\n      "lastName": {\n        "type": "string",\n        "description": "The person\'s last name."\n      }\n    }\n  }\n```\n\nwill be converted to:\n\n> # Person\n> *JSON Schema for a person object.*\n> ## Properties\n>\n> - **`firstName`** *(string)*: The person\'s first name.\n> - **`lastName`** *(string)*: The person\'s last name.\n\nSee the [examples](https://github.com/RalfG/jsonschema2md/tree/master/examples)\ndirectory for more elaborate examples.\n\n---\n\n## Installation\n\nInstall with pip\n\n```sh\npip install jsonschema2md\n```\n\n\n## Usage\n\n### From the CLI\n\n```sh\njsonschema2md [OPTIONS] <input.json> <output.md>\n```\n\n\n### From Python\n\n```python\nimport json\nimport jsonschema2md\n\nparser = jsonschema2md.Parser(\n    examples_as_yaml=False,\n    show_examples="all",\n)\nwith open("./examples/food.json", "r") as json_file:\n    md_lines = parser.parse_schema(json.load(json_file))\nprint(\'\'.join(md_lines))\n```\n\n\n### Options\n\n- `examples_as_yaml`: Parse examples in YAML-format instead of JSON. (`bool`, default:\n  `False`)\n- `show_examples`: Parse examples for only the main object, only properties, or all.\n(`str`, default `all`, options: `object`, `properties`, `all`)\n\n\n## Contributing\n\nBugs, questions or suggestions? Feel free to post an issue in the\n[issue tracker](https://github.com/RalfG/jsonschema2md/issues/) or to make a pull\nrequest! See\n[Contributing.md](https://github.com/RalfG/jsonschema2md/blob/master/CONTRIBUTING.md)\nfor more info.\n\n\n## Changelog\n\nSee [Changelog.md](https://github.com/RalfG/jsonschema2md/blob/master/CHANGELOG.md).\n',
    'author': 'Ralf Gabriels',
    'author_email': 'ralfg@hotmail.be',
    'maintainer': 'Stéphane Brunner',
    'maintainer_email': 'stephane.brunner@gmail.com',
    'url': 'https://github.com/sbrunner/jsonschema2md2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
