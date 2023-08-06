from loguru import logger
from typing import List

class DiscordServerMapping:
    def __init__(self):
        super().__init__()

    @staticmethod
    def detect_tags_server(data_object: dict, server_id_list: list) -> int:
        """
        Detect tags via matching server ids
        :param data_object: Discord data object
        :param server_id_list: server ID list
        :return: 1 if any server id matches, 0 otherwise
        """
        if data_object.get('server_id', 'NA') in server_id_list:
            return 1
        return 0

    def __call__(self, data_object: dict, server_id_list: list):
        return DiscordServerMapping.detect_tags_server(data_object, server_id_list)
