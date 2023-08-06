from typing import List
from .TextProcessing import TextProcessing

class TwitterPreprocessor:
    """
    Twitter-specific preprocessing logics
    """
    def __init__(self, preprocessor_config):
        self.preprocessor_config = preprocessor_config

    def process(self, data_object: dict) -> dict:
        if 'text' not in data_object:
            return data_object
        text_processor = TextProcessing([data_object['text']])
        processed_text = text_processor.clean_text()
        processed_text = processed_text[0]

        data_object['raw_text'] = data_object['text']
        data_object['text'] = processed_text
        return data_object

    def process_batch(self, data_objects: List[dict]) -> List[dict]:
        raw_texts = []
        for data_object in data_objects:
            if 'text' not in data_object:
                raw_texts.append('')
                continue
            raw_texts.append(data_object['text'])

        text_processor = TextProcessing(raw_texts)
        processed_texts = text_processor.clean_text()
        for i in range(len(data_objects)):
            data_objects[i]['raw_text'] = data_objects[i].get('text', '')
            data_objects[i]['text'] = processed_texts[i]
        return data_objects

    def __call__(self, data_object):
        if type(data_object) == dict:
            return self.process(data_object)
        elif type(data_object) == list:
            return self.process_batch(data_object)
        else:
            raise Exception(f"Unknown data type: {type(data_object)}")


if __name__ == '__main__':
    # Test
    preprocessor = TwitterPreprocessor({})
    print(preprocessor({"text": "Hello world!"}))
    print(preprocessor([{"text": "Hello world BTC&ETHHHH"}, {"text": "Hello world!"}, {"text": "Hello &amp world &amp"}]))
