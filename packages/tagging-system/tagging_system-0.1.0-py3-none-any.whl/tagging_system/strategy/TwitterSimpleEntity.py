from loguru import logger
from typing import List
import re


class TwitterSimpleEntity:
    def __init__(self):
        super().__init__()

    @staticmethod
    def detect_tags_entity(data_object, patterns,
                           include_text_entities=False,
                           include_context_annotations=True) -> int:
        """
        This method detects the tags in recognized  context annotations of a tweet.
        Scope:
            * Entities appeared in the text (hashtags, mentions, excluding URLs)
            * Entities appeared in the context annotation entity names
        :param data_object: the data object to be processed
        :param patterns: the patterns to be used
        :return:
        """

        if include_text_entities:
            text_entities = data_object.get('entities', [])

            # Hashtags
            if 'hashtags' in text_entities:
                for hashtag in text_entities['hashtags']:
                    hashtag_text = hashtag.get('tag', '')
                    for pattern in patterns:
                        if re.search(pattern=pattern, string=hashtag_text, flags=re.IGNORECASE):
                            return 1

        if include_context_annotations:
            context_annotations = data_object.get('context_annotations', [])
            for context_annotation in context_annotations:
                entity_name = context_annotation.get('entity', {}).get('name', '')
                entity_description = context_annotation.get('entity', {}).get('description', '')
                for pattern in patterns:
                    if re.search(pattern=pattern, string=entity_name, flags=re.IGNORECASE):
                        return 1
                    if re.search(pattern=pattern, string=entity_description, flags=re.IGNORECASE):
                        return 1

        return 0

    def __call__(self, data_object, patterns, include_text_entities=False, include_context_annotations=True):
        return TwitterSimpleEntity.detect_tags_entity(data_object, patterns, include_text_entities,
                                                      include_context_annotations)
