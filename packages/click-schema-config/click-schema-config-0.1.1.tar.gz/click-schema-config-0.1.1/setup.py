# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['click_schema_config']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0']

setup_kwargs = {
    'name': 'click-schema-config',
    'version': '0.1.1',
    'description': '',
    'long_description': '# click-schema-config\nclick-schema-config allows you to add settings from a config file. Those will be automatically pulled into your program description without having to repeat them. Comments will be used as helper text for click.\n\n# Installation\n```sh\npoetry add click-schema-config\n```\nor, using pip\n```\npip install click-schema-config\n```\n\n# Usage\nDecorate your function with\n```\n@schema_from_inis(filenames=[...])\n```\nThis will automatically infer the structure of your ini files and its documentation and add it to click.\n\nExample of a config.default.ini:\n```ini\ntestqwlj =\n\n[test1]\n; Wow, multilines\n; Talk about eye candy\nvar1="value1"\nvar2: int = 2\nvar3 = True\n\n[test2]\nvar1 = "value1" # Comment\n\n; This is a comment\n123j = None\n```\nNote that you can type values directly.\n\n```python\nimport pprint\nimport click\nfrom click_schema_config import schema_from_inis\n\n\n@click.command()\n@schema_from_inis(filenames=["config.default.ini"])\ndef main(**kwargs):\n    pprint.pprint(kwargs)\n\nif __name__ == "__main__":\n    main()\n```\n\nThis will result in:\n```sh\npython TODO.py --help\n\nUsage: TODO.py [OPTIONS]\n\nOptions:\n  --test2.123j TEXT               This is a comment\n  --test2.var1 TEXT\n  --test1.var3 / --no-test1.var3\n  --test1.var2 INTEGER\n  --test1.var1 TEXT               Wow, multilines Talk about eye candy\n  --testqwlj TEXT\n  --help                          Show this message and exit.\n```\n\nYou can of course override using the options:\n```sh\npython TODO.py --test2.123j hey\n\n{\'test1__var1\': \'value1\',\n \'test1__var2\': 2,\n \'test1__var3\': True,\n \'test2__123j\': \'hey\',\n \'test2__var1\': \'value1\',\n \'testqwlj\': None}\n```\n# Rationale\n[TODO]\n\n# TODO\n[TODO]\n',
    'author': 'Joy Void Joy',
    'author_email': 'joy.void.joy@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
