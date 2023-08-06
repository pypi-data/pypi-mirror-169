import re
from loguru import logger


class GenericSimpleRegex:
    def __init__(self):
        super().__init__()

    @staticmethod
    def detect_tags_regex(data_object, patterns,
                          field='text', regex_flags=re.IGNORECASE) -> int:
        """
        This method detects the tags using regex, and returns a list of results
        :param data_object: the data object to be processed
        :param patterns: the patterns to be used
        :param field: the field to be used (default: "text")
        :param regex_flags: the regex flags to be used (default: re.IGNORECASE)
        :return: 1 if any of the patterns matches, 0 otherwise
        """
        text = data_object.get(field, '')
        if type(patterns) is str:
            patterns = [patterns]
        for cur_pattern in patterns:
            match = re.search(pattern=cur_pattern, string=text, flags=regex_flags)
            if match is None:
                pass
            else:
                return 1
        return 0

    def __call__(self, data_object, patterns,
                 field='text', regex_flags=re.IGNORECASE) -> int:
        return GenericSimpleRegex.detect_tags_regex(data_object, patterns, field, regex_flags)
