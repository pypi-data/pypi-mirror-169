from typing import List
from loguru import logger
from ..strategy.GenericSimpleRegex import GenericSimpleRegex
from ..preprocessor.GenericPreprocessor import GenericPreprocessor
from ..aggregator.SimpleAggr import SimpleAggr

class GenericHandler:
    """
    Handler of general data objects
    """

    def __init__(self, config, ticker_config_list):
        self.config = config
        self.ticker_config_list = ticker_config_list

        self.ticker_config_dict = {}
        self.preprocess_pipeline = None
        self.aggregator = None

        self.generic_preprocessor = None

        self.init()

    @staticmethod
    def sanity_check_ticker_config(ticker_config: dict) -> bool:
        """
        Sanity check of ticker configs
        :param ticker_config: ticker config
        :return: True if ticker config is valid, False otherwise
        """

        logger.debug(f"Sanity checking ticker config: {ticker_config}")

        # Ticker config should have ticker
        if 'ticker' not in ticker_config:
            logger.warning(f"Ticker config does not have ticker: {ticker_config}")
            return False

        # Ticker should have at least one strategy configured for general data object
        generic_pipeline = ticker_config.get('data_source_config', {}).get('generic', {}).get('pipeline', [])
        if len(generic_pipeline) == 0:
            logger.warning(f"Ticker config does not have Generic strategy: {ticker_config}")
            return False

        return True

    def init(self):
        """
        Initialize handler, setup strategies when needed, and setup aggregators
        """

        # Sanity check, and convert ticker config list to dict
        self.ticker_config_dict = {}
        for cur_ticker_config in filter(GenericHandler.sanity_check_ticker_config, self.ticker_config_list):
            # Check if ticker duplicated
            if cur_ticker_config['ticker'] in self.ticker_config_dict:
                logger.warning(f"Ticker config duplicated: {cur_ticker_config}")
                continue

            self.ticker_config_dict[cur_ticker_config['ticker']] = cur_ticker_config
        logger.debug(f'Length of the sanitized ticker config dict: {len(self.ticker_config_dict)}')

        # Initialize preprocessor
        self.preprocess_pipeline = self.config.get('data_source_configs', {}).get('generic', {}).get(
            'preprocessing_pipeline', [])
        for cur_preprocessor in self.preprocess_pipeline:
            cur_preprocessor_type = cur_preprocessor.get('type', '')
            if cur_preprocessor_type == 'GenericPreprocessor':
                self.generic_preprocessor = GenericPreprocessor(self.config)
                break

        # Initialize aggregators
        self.aggregator = None
        aggr_config = self.config.get('data_source_configs', {}).get('generic', {}).get('aggregator')
        if aggr_config is not None:
            aggr_config_type = aggr_config.get('type', '')
            if aggr_config_type == 'SimpleAggr':
                self.aggregator = SimpleAggr(aggr_config)
            else:
                logger.warning(
                    f"Unknown aggregator type: {aggr_config_type}, no aggregation will be performed (raw output)")

    def identify_tickers(self, data_object) -> dict:
        """
        Identify tickers in a single (preprocessed) general data object
        :param data_object: input general data object
        :return: tag identification results (dict: {ticker: ticker_name, ticker_confidence: confidence})
        """

        logger.debug(f"Identifying tickers in data object: {data_object}")

        result = {}

        # Identify tickers in the data object
        for cur_ticker, cur_ticker_config in self.ticker_config_dict.items():
            # Create list slot for current ticker to store results
            result[cur_ticker] = []

            # Get strategy pipeline
            cur_ticker_pipeline = cur_ticker_config.get('data_source_config', {}).get('generic', {}).get('pipeline', [])
            logger.debug(f"Ticker: {cur_ticker}, pipeline: {cur_ticker_pipeline}")

            # Execute pipeline
            for cur_strategy in cur_ticker_pipeline:
                cur_strategy_type = cur_strategy.get('type', '')
                cur_result = {
                    'type': cur_strategy_type,
                    'weight': cur_strategy.get('weight', 1.0),
                    'result': None
                }
                if cur_strategy_type == 'GenericSimpleRegex':
                    cur_result['result'] = GenericSimpleRegex.detect_tags_regex(data_object,
                                                                                patterns=cur_strategy.get('patterns',
                                                                                                          []))
                else:
                    logger.warning(f"Unknown strategy: {cur_strategy}, skip")
                    continue

                if cur_result is not None:
                    result[cur_ticker].append(cur_result)
                    logger.debug(f"Strategy result: {cur_result}")

        logger.debug(f"Ticker identification results before aggregation: {result}")

        if self.aggregator is not None:
            # Aggregate ticker identification results
            result = self.aggregator(result)
            logger.debug(f"Ticker identification results: {result}")

        return result

    def batch_identify_tickers(self, data_object_list: list) -> List[dict]:
        """
        Identify tickers in a list of (preprocessed) general data objects
        :param data_object_list: list of general data objects
        :return: list of tag identification results
        """

        result_list = []
        for cur_data_object in data_object_list:
            result_list.append(self.identify_tickers(cur_data_object))

        return result_list

    def __call__(self, data_object):

        # Preprocess data object
        if self.preprocess_pipeline is not None:
            for cur_preprocessor in self.preprocess_pipeline:
                cur_preprocessor_type = cur_preprocessor.get('type', '')
                if cur_preprocessor_type == 'GenericPreprocessor':
                    data_object = self.generic_preprocessor(data_object)
                else:
                    logger.warning(f"Unknown preprocessor type: {cur_preprocessor_type}, skip")
                    continue

        if type(data_object) == dict:
            return self.identify_tickers(data_object)
        elif type(data_object) == list:
            return self.batch_identify_tickers(data_object)

