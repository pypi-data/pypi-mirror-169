import re
from loguru import logger


class DiscordSimpleRegex:
    def __init__(self):
        super().__init__()

    @staticmethod
    def detect_tags_regex(data_object, patterns) -> int:
        """
        This method detects the tags using regex, and returns a list of results
        :param data_object: the data object to be processed
        :param patterns: the patterns to be used
        :return: 1 if any of the patterns matches, 0 otherwise
        """
        text = data_object.get('content', '')
        if type(patterns) is str:
            patterns = [patterns]
        for cur_pattern in patterns:
            match = re.search(pattern=cur_pattern, string=text, flags=re.IGNORECASE)
            if match is None:
                pass
            else:
                return 1
        return 0

    def __call__(self, data_object, patterns):
        return DiscordSimpleRegex.detect_tags_regex(data_object, patterns)
