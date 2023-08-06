from loguru import logger

class SimpleAggr:
    def __init__(self, aggr_config):
        self.aggr_config = aggr_config

    def aggr_sum(self, result_object, weighted=True):
        result = {}

        # Iterate through tickers
        for ticker, ticker_results in result_object.items():
            cur_ticker_sum = 0
            # Sum up ticker results
            for cur_strategy_result in ticker_results:
                cur_weight = 1
                if weighted:
                    if "weight" not in cur_strategy_result:
                        logger.warning(f"Missing weight in strategy result: {cur_strategy_result}, fallback to 1")
                    cur_weight = cur_strategy_result['weight']
                cur_ticker_sum += cur_strategy_result['result'] * cur_weight

            if cur_ticker_sum > 0:
                result[ticker] = cur_ticker_sum
        return result

    def aggr_max(self, result_object, weighted=True):
        result = {}

        # Iterate through tickers
        for ticker, ticker_results in result_object.items():
            cur_ticker_max = 0
            # take max from ticker results
            for cur_strategy_result in ticker_results:
                cur_weight = 1
                if weighted:
                    if "weight" not in cur_strategy_result:
                        logger.warning(f"Missing weight in strategy result: {cur_strategy_result}, fallback to 1")
                    cur_weight = cur_strategy_result['weight']
                cur_ticker_max = max(cur_ticker_max, cur_strategy_result['result'] * cur_weight)

            if cur_ticker_max > 0:
                result[ticker] = cur_ticker_max

        return result

    def aggregate(self, result_object):
        logger.debug(f"Aggregating: {result_object}")

        aggr_mode = self.aggr_config.get('mode', '')
        if aggr_mode == 'sum':
            return self.aggr_sum(result_object, weighted=self.aggr_config.get('weighted', False))
        elif aggr_mode == 'max':
            return self.aggr_max(result_object, weighted=self.aggr_config.get('weighted', False))
        else:
            logger.warning(f"Unknown aggr_mode: {aggr_mode}, fallback to sum")
            return self.aggr_sum(result_object, weighted=self.aggr_config.get('weighted', False))

    def __call__(self, result_object):
        return self.aggregate(result_object)
