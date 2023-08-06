from loguru import logger
from typing import List


class TwitterSimpleUserMapping:
    def __init__(self):
        super().__init__()

    @staticmethod
    def detect_tags_user(data_object: dict, user_id_list: list,
                         include_author=True,
                         include_mentioned=True,
                         include_reply_to=True) -> int:
        """
        Detect tags via matching user ids, covering the following scenarios:
            * A user if the author of the tweet
            * A user is mentioned by the tweet
            * A user is the reply to a tweet
        :param data_object: Twitter data object
        :param user_id_list: user ID list (not user name)
        :param include_author: should the author be included in the result
        :param include_mentioned: should the mentioned users be included in the result
        :param include_reply_to: should the reply-to users be included in the result
        :return: 1 if any user id matches, 0 otherwise
        """
        if include_author:
            if data_object.get('author_id', 'NA') in user_id_list:
                return 1
        if include_mentioned:
            mentioned_users = data_object.get('entities', {}).get('mentions', [])
            for mentioned_user in mentioned_users:
                if mentioned_user.get('id', 'NA') in user_id_list:
                    return 1
        if include_reply_to:
            if data_object.get('in_reply_to_user_id', 'NA') in user_id_list:
                return 1
        return 0

    def __call__(self, data_object: dict, user_id_list: list,
                 include_author=True,
                 include_mentioned=True,
                 include_reply_to=True):
        return TwitterSimpleUserMapping.detect_tags_user(data_object, user_id_list,
                                                         include_author,
                                                         include_mentioned,
                                                         include_reply_to)
