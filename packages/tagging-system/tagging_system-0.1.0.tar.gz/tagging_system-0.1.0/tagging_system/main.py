import argparse
from loguru import logger
import json
import os
from tagging_system.handler.TwitterHandler import TwitterHandler

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, default='./config.json', help='config JSON path')
    return parser.parse_args()



def test_in_folder_twitter(data_path, twitter_handler, batch_size=100):
    logger.debug(f'[test_in_folder] {data_path}')

    # Recursively list all JSON files in the folder
    file_list = []
    for root, dirs, files in os.walk(data_path):
        logger.debug(f'root: {root}, dirs: {dirs}, files: {files}')
        for cur_file in files:
            if cur_file.endswith('.json'):
                file_list.append(os.path.join(root, cur_file))

    logger.debug(f'Found {len(file_list)} JSON files in {data_path}')

    # Load data objects into batches and test
    cur_batch_start_idx = 0
    while cur_batch_start_idx < len(file_list):
        cur_batch_end_idx = min(cur_batch_start_idx + batch_size, len(file_list))
        cur_batch_files = file_list[cur_batch_start_idx:cur_batch_end_idx]
        cur_batch_data = []
        for cur_file in cur_batch_files:
            with open(cur_file, 'r') as f:
                cur_batch_data.append(json.load(f))

        cur_batch_data = twitter_handler(cur_batch_data)
        logger.debug(f'[test_in_folder] {cur_batch_data}')

        cur_batch_start_idx = cur_batch_end_idx

@logger.catch
def main():
    # Read config
    args = parse_args()
    config = {}
    try:
        with open(args.config, 'r') as f:
            config = json.load(f)
            logger.debug(f'[config] {config}')
    except FileNotFoundError:
        logger.debug('config.json not found, will create new one')
        pass
    except Exception as e:
        logger.error('Failed to load config.json')
        raise e

    # Load ticker configs
    logger.debug('Loading ticker')
    ticker_config_list = []
    ticker_config_path = config.get('ticker_config_path', './ticker_config')
    for root, dirs, files in os.walk(ticker_config_path):
        logger.debug(f'root: {root}, dirs: {dirs}, files: {files}')
        for cur_file in files:
            if cur_file.endswith('.json'):
                with open(os.path.join(root, cur_file), 'r') as f:
                    ticker_config_list.append(json.load(f))
    logger.debug(f'Found {len(ticker_config_list)} ticker configs')


    # Initalize handlers
    twitter_handler = TwitterHandler(config, ticker_config_list)

    # Perform test
    if config.get('test_mode') == 'folder':
        test_in_folder_twitter(config.get('test_data_path'), twitter_handler)


if __name__ == '__main__':
    main()
