from loguru import logger
from typing import List

class DiscordChannelMapping:
    def __init__(self):
        super().__init__()

    @staticmethod
    def detect_tags_channel(data_object: dict, channel_id_list: list) -> int:
        """
        Detect tags via matching channel ids
        :param data_object: Discord data object
        :param channel_id_list: channel ID list
        :return: 1 if any channel id matches, 0 otherwise
        """
        if data_object.get('channel_id', 'NA') in channel_id_list:
            return 1
        return 0

    def __call__(self, data_object: dict, channel_id_list: list):
        return DiscordChannelMapping.detect_tags_channel(data_object, channel_id_list)
