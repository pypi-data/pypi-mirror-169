# Tagging system

## Overview

![](https://github.com/MetaSearch-IO/TaggingSystem/blob/master/assets/TaggingSys_sch.png)

The tagging system is composed by the following major components:
* **Preprocessors**: preprocesses the input data objects before tagging.
* **Tag ID strategies**: independent strategies to identify tags from input data objects
* **Aggregators**: post-process and aggregates the tagging results from tag ID pipelines configured for each assets
* **Handlers**: assembles preprocessor, tag ID pipelines, and result aggregation logics for each type of data source

### Input of the tagging system

Currently, the system is implemented to receive batches of data objects from various data sources, e.g., Twitter (
implemented), Discord (TBI), Medium (TBI), Reddit (TBI), etc.

### Preprocessors

Preprocessors are used to preprocess the input data objects before tagging. 

### Strategies

Strategies are used to identify tags from input (pre-processed) data objects. Strategies are expected to work independently,
and will work per-asset. 

### Aggregators

Aggregators are used to post-process and aggregate the tagging results from tag ID pipelines configured for each assets.
Cross-asset tagging strategies should also be implemented here. Aggregators are expected to have access to all outputs
from tagging strategies (asset-wise), and the input data objects.

### Handlers

Handlers control the flows of the actual tagging process for each data source. The handler reads preprocessing pipeline
and aggregation pipeline from the `data_source_configs` of global config, and reads tag identification pipelines from
ticker-specific configurations. 

## Applying TaggingSystem in downstream logics

1. Prepare `tagger` configs in a JSON file, e.g., `config.json`. You may find a sample in: https://github.com/MetaSearch-IO/TaggingSystem/blob/master/sample_configs/config.json . This config file contains global settings for all tickers, including: preprocessing pipeline, and ticker idenfication results aggregation pipeline. Read this config as:
```py
config = json.load(open('config.json'))
```
2. Prepare a list of ticker specific configs, e.g., `ticker_configs.json`. You may find a lot of prepared configs in https://github.com/MetaSearch-IO/TickerConfigs . Read this config as:
```py
# In this example we only read one ticker config
ticker_config_list = json.load(open('ticker_configs/curated_tickers/Chains/ETH.json'))
```

3. Initialize a `Handler` object, and tag your data object(s) by calling it on the data object(s):

```py
from TaggingSystem.handler.DiscordHandler import DiscordHandler

# Init handler
crypto_ticker_tagger = DiscordHandler(config=config, ticker_config_list=ticker_config_list)

# Sample data, could also be a list of dicts
processed_data = {"content": "test BTC"}

# Apply Tagging Logic
crypto_tickers = crypto_ticker_tagger(processed_data)

# crypto_tickers = [{'BTC': 1.0}]
```
