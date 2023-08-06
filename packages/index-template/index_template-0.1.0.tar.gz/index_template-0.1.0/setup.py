# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['index_template']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.0,<0.6.0', 'requests>=2.28,<3.0']

setup_kwargs = {
    'name': 'index-template',
    'version': '0.1.0',
    'description': '',
    'long_description': '# IndexTemplate\n1. This repository contains MetaSearch index template definitions and util methods as shared resources.\n2. It also provides an index creation script to manually create index tempalte for Twitter and Discord search (TODO: integrate index template creation as part of OpenSearch CDK deployement)\n\n## To create index template\n1. Enter your OpenSearch URI, username and password in index_configs.py\n2. Run "python3 setup.py install --user && python3 src/create_templates.py"\n\n## To modify index field definitions\n1. In "field_definitions.py", identify if it\'s a shared field or any verticial specific field, and modify the corresponding variables\n\n## To obtain the list of index fields for a specific index in downstream indexer code\n1. Import this repository using Git Submodule\n2. Import the necessary index config `from index_configs import twitter_index_config`\n3. Use the get fields method `get_fields_by_index(discord_index_config).keys()`\n\n## To obtain the index to be updated or other index metadata\n1. Import "twitter_index_config" or "discord_index_config" and look for the associated attributes\n2. The index name to be updated to can be found at "twitter_index_config.index_name" and "discord_index_config.index_name"\n\n## Notes on re-indexing\n1. For lightweight re-indexing after template change, follow https://opensearch.org/docs/latest/opensearch/reindex-data/\n\n## TODO\n1. Test the util in indexing lambda using submodules to ensure indexer can be kept in sync with index template, and index based on the template accordingly\n',
    'author': 'kaito-hao',
    'author_email': 'anya@kaito.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MetaSearch-IO/IndexTemplate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
