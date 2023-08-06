from typing import List
from loguru import logger
from ..strategy.DiscordUserMapping import DiscordUserMapping
from ..strategy.DiscordChannelMapping import DiscordChannelMapping
from ..strategy.DiscordSimpleRegex import DiscordSimpleRegex
from ..strategy.DiscordServerMapping import DiscordServerMapping
from ..aggregator.SimpleAggr import SimpleAggr
from ..preprocessor.DiscordPreprocessor import DiscordPreprocessor


class DiscordHandler:
    """
    Handler of discord data objects
    """

    def __init__(self, config, ticker_config_list):
        self.config = config
        self.ticker_config_list = ticker_config_list

        self.ticker_config_dict = {}
        self.preprocess_pipeline = None
        self.aggregator = None

        self.discord_preprocessor = None

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

        # Ticker should have at least one strategy configured for Discord
        discord_pipeline = ticker_config.get('data_source_config', {}).get('discord', {}).get('pipeline', [])
        if len(discord_pipeline) == 0:
            logger.warning(f"Ticker config does not have Discord strategy: {ticker_config}")
            return False

        return True

    def init(self):
        """
        Initialize handler, setup strategies when needed, and setup aggregators
        """

        # Sanity check, and convert ticker config list to dict
        self.ticker_config_dict = {}
        for cur_ticker_config in filter(DiscordHandler.sanity_check_ticker_config, self.ticker_config_list):
            # Check if ticker duplicated
            if cur_ticker_config['ticker'] in self.ticker_config_dict:
                logger.warning(f"Ticker config duplicated: {cur_ticker_config}")
                continue

            self.ticker_config_dict[cur_ticker_config['ticker']] = cur_ticker_config
        logger.debug(f'Length of the sanitized ticker config dict: {len(self.ticker_config_dict)}')

        # Initialize preprocessor
        self.preprocess_pipeline = self.config.get('data_source_configs', {}).get('discord', {}).get(
            'preprocessing_pipeline', [])
        for cur_preprocessor in self.preprocess_pipeline:
            cur_preprocessor_type = cur_preprocessor.get('type', '')
            if cur_preprocessor_type == 'DiscordPreprocessor':
                self.discord_preprocessor = DiscordPreprocessor(self.config)
                break

        # Initialize aggregators
        self.aggregator = None
        aggr_config = self.config.get('data_source_configs', {}).get('discord', {}).get('aggregator')
        if aggr_config is not None:
            aggr_config_type = aggr_config.get('type', '')
            if aggr_config_type == 'SimpleAggr':
                self.aggregator = SimpleAggr(aggr_config)
            else:
                logger.warning(
                    f"Unknown aggregator type: {aggr_config_type}, no aggregation will be performed (raw output)")

    def identify_tickers(self, data_object) -> dict:
        """
        Identify tickers in a single (preprocessed) discord data object
        :param data_object: input discord data object
        :return: tag identification results (dict: {ticker: ticker_name, ticker_confidence: confidence})
        """

        logger.debug(f"Identifying tickers in data object: {data_object}")

        result = {}

        # Identify tickers in the data object
        for cur_ticker, cur_ticker_config in self.ticker_config_dict.items():
            # Create list slot for current ticker to store results
            result[cur_ticker] = []

            # Get strategy pipeline
            cur_ticker_pipeline = cur_ticker_config.get('data_source_config', {}).get('discord', {}).get('pipeline', [])
            logger.debug(f"Ticker: {cur_ticker}, pipeline: {cur_ticker_pipeline}")

            # Execute pipeline
            for cur_strategy in cur_ticker_pipeline:
                cur_strategy_type = cur_strategy.get('type', '')
                cur_result = {
                    'type': cur_strategy_type,
                    'weight': cur_strategy.get('weight', 1.0),
                    'result': None
                }
                if cur_strategy_type == 'DiscordSimpleRegex':
                    cur_result['result'] = DiscordSimpleRegex.detect_tags_regex(data_object,
                                                                                patterns=cur_strategy.get('patterns',
                                                                                                          []))
                elif cur_strategy_type == 'DiscordUserMapping':
                    cur_result['result'] = DiscordUserMapping.detect_tags_user(data_object,
                                                                               user_id_list=cur_strategy.get('user_ids',
                                                                                                             []),
                                                                               include_author=cur_strategy.get(
                                                                                   'include_author', True),
                                                                               include_mentioned=cur_strategy.get(
                                                                                   'include_mentioned', True))
                elif cur_strategy_type == 'DiscordChannelMapping':
                    cur_result['result'] = DiscordChannelMapping.detect_tags_channel(data_object,
                                                                                     channel_id_list=cur_strategy.get(
                                                                                         'channel_ids', []))
                elif cur_strategy_type == 'DiscoreServerMapping':
                    cur_result['result'] = DiscordServerMapping.detect_tags_server(data_object,
                                                                                    server_id_list=cur_strategy.get(
                                                                                        'server_ids', []))
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
        Identify tickers in a list of (preprocessed) discord data objects
        :param data_object_list: list of discord data objects
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
                if cur_preprocessor_type == 'DiscordPreprocessor':
                    data_object = self.discord_preprocessor(data_object)
                else:
                    logger.warning(f"Unknown preprocessor type: {cur_preprocessor_type}, skip")
                    continue

        if type(data_object) == dict:
            return self.identify_tickers(data_object)
        elif type(data_object) == list:
            return self.batch_identify_tickers(data_object)
