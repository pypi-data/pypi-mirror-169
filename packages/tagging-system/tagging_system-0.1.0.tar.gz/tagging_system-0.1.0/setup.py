# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tagging_system',
 'tagging_system.aggregator',
 'tagging_system.handler',
 'tagging_system.preprocessor',
 'tagging_system.strategy']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.10,<5.0',
 'loguru>=0.5.0,<0.6.0',
 'lxml>=4.9.1,<5.0.0',
 'markdown>=3.4.1,<4.0.0',
 'nltk>=3.7,<4.0',
 'requests>=2.28,<3.0']

setup_kwargs = {
    'name': 'tagging-system',
    'version': '0.1.0',
    'description': '',
    'long_description': '# Tagging system\n\n## Overview\n\n![](https://github.com/MetaSearch-IO/TaggingSystem/blob/master/assets/TaggingSys_sch.png)\n\nThe tagging system is composed by the following major components:\n* **Preprocessors**: preprocesses the input data objects before tagging.\n* **Tag ID strategies**: independent strategies to identify tags from input data objects\n* **Aggregators**: post-process and aggregates the tagging results from tag ID pipelines configured for each assets\n* **Handlers**: assembles preprocessor, tag ID pipelines, and result aggregation logics for each type of data source\n\n### Input of the tagging system\n\nCurrently, the system is implemented to receive batches of data objects from various data sources, e.g., Twitter (\nimplemented), Discord (TBI), Medium (TBI), Reddit (TBI), etc.\n\n### Preprocessors\n\nPreprocessors are used to preprocess the input data objects before tagging. \n\n### Strategies\n\nStrategies are used to identify tags from input (pre-processed) data objects. Strategies are expected to work independently,\nand will work per-asset. \n\n### Aggregators\n\nAggregators are used to post-process and aggregate the tagging results from tag ID pipelines configured for each assets.\nCross-asset tagging strategies should also be implemented here. Aggregators are expected to have access to all outputs\nfrom tagging strategies (asset-wise), and the input data objects.\n\n### Handlers\n\nHandlers control the flows of the actual tagging process for each data source. The handler reads preprocessing pipeline\nand aggregation pipeline from the `data_source_configs` of global config, and reads tag identification pipelines from\nticker-specific configurations. \n\n## Applying TaggingSystem in downstream logics\n\n1. Prepare `tagger` configs in a JSON file, e.g., `config.json`. You may find a sample in: https://github.com/MetaSearch-IO/TaggingSystem/blob/master/sample_configs/config.json . This config file contains global settings for all tickers, including: preprocessing pipeline, and ticker idenfication results aggregation pipeline. Read this config as:\n```py\nconfig = json.load(open(\'config.json\'))\n```\n2. Prepare a list of ticker specific configs, e.g., `ticker_configs.json`. You may find a lot of prepared configs in https://github.com/MetaSearch-IO/TickerConfigs . Read this config as:\n```py\n# In this example we only read one ticker config\nticker_config_list = json.load(open(\'ticker_configs/curated_tickers/Chains/ETH.json\'))\n```\n\n3. Initialize a `Handler` object, and tag your data object(s) by calling it on the data object(s):\n\n```py\nfrom TaggingSystem.handler.DiscordHandler import DiscordHandler\n\n# Init handler\ncrypto_ticker_tagger = DiscordHandler(config=config, ticker_config_list=ticker_config_list)\n\n# Sample data, could also be a list of dicts\nprocessed_data = {"content": "test BTC"}\n\n# Apply Tagging Logic\ncrypto_tickers = crypto_ticker_tagger(processed_data)\n\n# crypto_tickers = [{\'BTC\': 1.0}]\n```\n',
    'author': 'kaito-hao',
    'author_email': 'anya@kaito.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MetaSearch-IO/TaggingSystem',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
