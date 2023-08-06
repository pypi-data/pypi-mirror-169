import html
import logging
import re
from typing import List

import nltk
from bs4 import BeautifulSoup
from markdown import markdown
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from .TextProcessingLiterals import contractions_map, exclude_words, time_zones

## One solution is to use Lambda's ephemeral storage at the location /tmp, However, this likely isn't a great solution if you have huge concurrency.
nltk.data.path.append("/tmp")

nltk.download("punkt", download_dir="/tmp")
nltk.download("stopwords", download_dir="/tmp")
nltk.download("wordnet", download_dir="/tmp")
nltk.download("averaged_perceptron_tagger", download_dir="/tmp")


class TextProcessing:
    def __init__(self, raw_data: List[str]):
        """
        This is the constructor for TextProcessing class

        Parameters:
        -----------
            raw_data (List[str]):
                List of text that needs to be cleaned

        Raises:
        -------
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        if type(raw_data) is list:
            try:
                self.raw_data = raw_data

            except Exception as e:
                logging.exception(e)
                print(
                    """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
                )

    @staticmethod
    def remove_headers(text: str) -> str:
        """
        This method removes headers (either embedded in markdown format or as plain text) from a text

        Parameters:
        -----------
            text (str):
                Raw text that needs to be processed

        Returns:
        -------
            (str):
                text without headers
        """

        # parse markdown as html
        html_text = markdown(text)
        # parse text in lxml format
        soup_text = BeautifulSoup(html_text, "lxml")
        # find all headers and create a list of those tags
        headers = soup_text.find_all(["h1", "h2", "h3", "h4", "h5", "h6", "strong", "b"])
        headers_list = [header.get_text().strip() for header in headers]
        # remove those tags anad append text to a list
        clean_text = " ".join([string for string in soup_text.stripped_strings if string not in headers_list])
        # remove numbered lists that are headers and are not parsed as numbered lists or as bold because it is in plain text
        # manually identifies lines that start with a single digit followed by '.' or ')' or '>' and ends with question mark
        # for example, 1) How was the event detected?
        # These questions might be repetitive across different COEs and hence removing them
        numbered_headers_list = re.findall(r"[0-9][.>)].*\?", text, flags=re.MULTILINE)
        # re.compile compiles a regex expression into a regex object
        # numbered_headers_list is a list of sentences
        # For example, ['1) How was the event detected?', '1. Why was there an availability drop?']
        # To replace these sentences with "", escape each word in a sentence and concatenate sentences in a list with '|'
        # This entire expression is then compiled as a regex expression which is then substitued in the text with ""
        regex_expression = re.compile("|".join(map(re.escape, numbered_headers_list)))
        clean_text = regex_expression.sub("", clean_text)

        return clean_text

    @staticmethod
    def remove_links(text: str) -> str:
        """
        This method removes links (either embedded in markdown format or as plain text) from a text

        Parameters:
        -----------
            text (str):
                raw text that needs to be processed

        Returns:
        -------
            (str):
                text without links
        """

        # parse markdown as html
        html_text = markdown(text)
        # parse text in lxml format
        soup_text = BeautifulSoup(html_text, "lxml")
        # find all links and create a list of those tags
        links = soup_text.find_all("a")
        links_list = [link.get_text().strip() for link in links]
        # remove those tags anad append the text to a list
        clean_text = " ".join([string for string in soup_text.stripped_strings if string not in links_list])
        # remove links that are in plain text
        clean_text = re.sub(r"http[s]?:\S+", "", clean_text)

        return clean_text

    @staticmethod
    def fix_punctuation(text: str) -> str:
        """
        This method fixes multipl eoccurences of punctuation ('!', '?', '.', ',', ':') that are mistyped
        For example: Hello!!! -> Hello!

        Parameters:
        -----------
            text (str):
                Raw text

        Returns:
        -------
            (str):
                Standardized text with punctuations fixed, if any
        """

        clean_text = re.sub(
            r"\s+\:+|\:+",
            ":",
            re.sub(
                r"\s+\!+|\!+",
                "!",
                re.sub(r"\s+\,+|\,+", ",", re.sub(r"\s+\?+|\?+", "?", re.sub(r"\s+\.+|\.+", "", text))),
            ),
        )
        return clean_text

    @staticmethod
    def standardize_quotes(text: str) -> str:
        """
        This method standardizes quotation in the text. Replace curly quotes with quotes
        For example: It’s -> It's

        Parameters:
        -----------
            text (str):
                Raw text

        Returns:
        -------
            (str):
                text with standardized quotes, if any
        """

        clean_text = re.sub(r"\s+\’+|\’+", "'", re.sub(r"\s+\‘+|\‘+", "'", text))
        return clean_text

    @staticmethod
    def expand_contractions(text: str) -> str:
        """
        This method expands any contractions found in the text
        Contractions are shortened version of words or syllables
        For example: would've -> would have

        Parameters:
        -----------
            text (str):
                Raw text that needs to be standardized by expanding contractions

        Returns:
        -------
            (str):
                Standardized text with expanded contractions, if any
        """

        # re.compile compiles a regex expression into a regex object
        # contraction_mapping is a dictionary contractions and their corresponding expanded form
        # To replace the key with values from the map, concatenate keys of a map with '|'
        # This entire expression is then compiled as a regex expression which is then substitued in the text with map values
        # Example output: re.compile("(ain't|aren't|can't|can't've)", flags=re.IGNORECASE|re.DOTALL)
        contractions_regex_pattern = re.compile(
            "({})".format("|".join(contractions_map.keys())), flags=re.IGNORECASE | re.DOTALL
        )

        def get_expanded_contraction(contraction):
            """
            This method finds a match in the text and retrieves corresponding expanded value from the map

            Parameters:
            -----------
                contraction (re.match):
                    regex match object in the text

            Returns:
            -------
                (str):
                    expanded contractions for matching keys
            """

            # group(0) retrieves matched strings in the text
            match = contraction.group(0)
            # get the corresponding value (expanded contraction) from the map
            expanded_contraction = (
                contractions_map.get(match) if contractions_map.get(match) else contractions_map.get(match.lower())
            )

            return expanded_contraction

        # For replace, function "get_expanded_contraction" is called for every non-overlapping occurrence of pattern
        # This function takes a single match object argument, and returns the replacement string
        expanded_text = contractions_regex_pattern.sub(get_expanded_contraction, text)

        return expanded_text

    def clean_text(self) -> List[str]:
        """
        This method cleans the list of texts

        Parameters:
        -----------
            raw_data (List[str]):
                List of text that needs to be cleaned

        Returns:
        -------
            (List[str]):
                list of processed strings
        """

        text_list = self.raw_data
        clean_text_list = []

        for text in text_list:
            clean_text = text
            # remove brackets
            clean_text = re.sub(r"[\\[\\]{}()&]", " ", clean_text)
            # remove new lines
            clean_text = re.sub(r"(\n\s*)+\n", "\n", clean_text)
            # remove spaces
            clean_text = re.sub(r" {2,}", " ", clean_text)
            # remove html tags if any
            clean_text = re.sub(r"[\<].*?[\>]", " ", clean_text)
            # fix multiple occurences of punctuation marks
            clean_text = TextProcessing.fix_punctuation(clean_text)
            # standardize quotation marks in the text
            clean_text = TextProcessing.standardize_quotes(clean_text)
            # replace contractions with their expanded form to standardize text
            clean_text = TextProcessing.expand_contractions(clean_text)
            # replace question and exclamation marks with '.' to determine sentences
            clean_text = re.sub(r"[\?|\!]", "", clean_text)
            # retain alpha-numeric characters, and characters ('.', "'", ':', '-') to determine sentences and date/timestamps
            clean_text = re.sub(r"[^A-Za-z0-9'\.\':-]+", " ", clean_text)
            # exclude words less than 2 letters
            clean_text = " ".join([word.strip() for word in clean_text.split(" ") if len(word) > 2])
            # add text to final list
            clean_text_list.append(clean_text)

        return clean_text_list

    @staticmethod
    def word_tokenizer(clean_text: List[str]) -> List[List[str]]:
        """
        This method tokenizes every word in the text

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[List[str]]):
                list of tokens

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        # create an empty list to append texts
        tokens_list = []

        try:
            if type(clean_text) is list:

                try:
                    for text in clean_text:
                        tokens = word_tokenize(text)
                        tokens_list.append(tokens)

                except Exception as e:
                    logging.exception(e)
                    print(""" \n List is empty. Provide a list of text. \n""")

        except Exception as e:
            logging.exception(e)
            print(
                """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
            )

        return tokens_list

    @staticmethod
    def remove_stop_words(clean_text: List[str], stop_words_list: List[str] = None, flag: str = "both") -> List[str]:
        """
        This method returns text without stop words

        Parameters:
        -----------
            clean_text (List[str]):
                list of text
            stop_words_list (List[str]):
                custom list of stop words. Defaults to None
            flag (str):
                This parameter takes a binary input (only/both). Defaults to "both"
                This parameter is processed only when a custom stop words list is provided
                By default, when a custom list is provided it does a union of stop words from nltk library and the custom list
                If it is required to remove only the list of words provided in stop_words_list, then choose option "only"

        Returns:
        -------
            (List[str]):
                list of text without stop words

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
        """

        if stop_words_list is None:
            stop_words_list = []

        stop = stopwords.words("english")
        # excluding some useful words from stop words list (to identify negative impact)
        stop_words = [word for word in stop if word not in exclude_words]
        # adding timezones to list of stop words
        stop_words = stop_words + time_zones + [x.lower() for x in time_zones]

        # create an empty list to append texts
        clean_text_list = []
        # create an empty string
        tokens_text = ""

        try:
            for text in clean_text:
                # if a custom stop list is provided, then do the following
                if stop_words_list:
                    # check the value of 'flag'
                    # if 'only' is the input, just remove words in the custom list provided
                    if flag == "only":
                        stop_words = stop_words_list
                    # if value is 'both', do a union of stop words and custom stop words
                    elif flag == "both":
                        stop_words = list(set(stop_words + stop_words_list))
                    tokens = TextProcessing.word_tokenizer([text])
                    tokens_text = " ".join(
                        [item for sublist in [t for t in tokens] for item in sublist if item not in stop_words]
                    )
                    clean_text_list.append(tokens_text)

                else:
                    tokens = TextProcessing.word_tokenizer([text])
                    tokens_text = " ".join(
                        [item for sublist in [t for t in tokens] for item in sublist if item not in stop_words]
                    )
                    clean_text_list.append(tokens_text)

        except Exception as e:
            logging.exception(e)
            print(""" \n List is empty. Provide a list of text. \n""")

        return clean_text_list

    @staticmethod
    def sentence_tokenizer(clean_text: List[str]) -> List[List[str]]:
        """
        This method splits text into a list of sentences

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[List[str]]):
                list of sentences

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        # create an empty list to append texts
        tokens_list = []
        try:
            if type(clean_text) is list:

                try:
                    for text in clean_text:
                        tokens = sent_tokenize(text)
                        tokens_list.append(tokens)

                except Exception as e:
                    logging.exception(e)
                    print(""" \n List is empty. Provide a list of text. \n""")

        except Exception as e:
            logging.exception(e)
            print(
                """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
            )

        return tokens_list

    @staticmethod
    def lower_case(clean_text: List[str]) -> List[str]:
        """
        This method converts words into lower-case except for words that are capitalized (acronyms)

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[str]):
                list of text with all words in lower-case except acronyms

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
        """

        # create an empty list to append texts
        final_list = []

        try:
            for text in clean_text:
                # create a list of token for every text in the list
                tokens_list = [
                    item for sublist in [word for word in TextProcessing.word_tokenizer([text])] for item in sublist
                ]
                # create an empty list to append texts
                lower_case_list = []
                # create an empty text
                lower_case_text = ""

                for word in tokens_list:
                    if word.isupper():
                        lower_case_list.append(word)
                    else:
                        lower_case_list.append(word.lower())
                    lower_case_text = " ".join(lower_case_list)

                final_list.append(lower_case_text)

        except Exception as e:
            logging.exception(e)
            print(""" \n List is empty. Provide a list of text. \n""")

        return final_list

    @staticmethod
    def alpha_numeric_text(clean_text: List[str]) -> List[str]:
        """
        This method retains only alpha-numeric characters in a text

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[str]):
                list of processed text with only alpha-numeric characters

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        # create an empty list to append texts
        final_list = []

        try:
            if type(clean_text) is list:
                try:
                    for text in clean_text:
                        alpha_numeric_text = text.replace("'", "")
                        alpha_numeric_text = re.sub(r"[^A-Za-z0-9']+", " ", alpha_numeric_text)
                        final_list.append(alpha_numeric_text)

                except Exception as e:
                    logging.exception(e)
                    print(""" \n List is empty. Provide a list of text. \n""")

        except Exception as e:
            logging.exception(e)
            print(
                """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
            )

        return final_list

    @staticmethod
    def get_wordnet_pos_tag(word: str) -> str:
        """
        This method extracts POS tags for the word provided

        Parameters:
        -----------
            word (str):
                A single word

        Returns:
        -------
            (str):
                a letter representing a POS tag (n:noun, j:adjective, v:verb, r:adverb)
        """

        # gets the first chanracter of the POS tag returned
        # For example, NNP -> N; VBG -> V
        pos_tag = nltk.pos_tag([word])[0][1][0].upper()
        # create a dictionary of only POS tags that are accepted by lemmatization
        pos_tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB, "R": wordnet.ADV}

        return pos_tag_dict.get(pos_tag, wordnet.NOUN)

    @staticmethod
    def stem_text(clean_text: List[str]) -> List[str]:
        """
        This method stems words in the text. It uses SnowballStemmer library to perform stemming

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[str]):
                list of stemmed text

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        snow = SnowballStemmer("english")

        # create an empty list to append texts
        stemmed_text_list = []

        try:
            if type(clean_text) is list:

                try:
                    for text in clean_text:
                        # create an empty list to append texts
                        stemmed_word_list = []
                        # create an empty string
                        stemmed_text = ""
                        # create a list of tokens
                        tokens_list = [
                            item
                            for sublist in [word for word in TextProcessing.word_tokenizer([text])]
                            for item in sublist
                        ]

                        # stemming automatically converts all words to lower-case. To preserve acronyms, the following is done
                        for word in tokens_list:
                            if word == word.upper():
                                stemmed_word = snow.stem(word).upper()
                            elif word == word.capitalize():
                                stemmed_word = snow.stem(word).capitalize()
                            else:
                                stemmed_word = snow.stem(word)

                            stemmed_word_list.append(stemmed_word)
                            stemmed_text = " ".join(stemmed_word_list)

                        stemmed_text_list.append(stemmed_text)

                except Exception as e:
                    logging.exception(e)
                    print(""" \n List is empty. Provide a list of text. \n""")

        except Exception as e:
            logging.exception(e)
            print(
                """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
            )

        return stemmed_text_list

    @staticmethod
    def lemmatize_text(clean_text: List[str]) -> List[str]:
        """
        This method lemmatizes words in the text. It uses WordNetLemmatizer from nltk library to perform lemmatization

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[str]):
                list of lemmatized text

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        wl = WordNetLemmatizer()

        # create an empty list to append texts
        lemmatized_text_list = []

        try:
            if type(clean_text) is list:

                try:
                    for text in clean_text:
                        # create a list of tokens
                        tokens_list = [
                            item
                            for sublist in [word for word in TextProcessing.word_tokenizer([text])]
                            for item in sublist
                        ]
                        # lemmatize words based on appropriate POS tags
                        lemmatized_text = " ".join(
                            [wl.lemmatize(word, TextProcessing.get_wordnet_pos_tag(word)) for word in tokens_list]
                        )
                        lemmatized_text_list.append(lemmatized_text)

                except Exception as e:
                    logging.exception(e)
                    print(""" \n List is empty. Provide a list of text. \n""")

        except Exception as e:
            logging.exception(e)
            print(
                """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
            )

        return lemmatized_text_list

    @staticmethod
    def extract_acronyms(clean_text: List[str]) -> List[List[str]]:
        """
        This method extracts acronyms from a text

        Parameters:
        -----------
            clean_text (List[str]):
                list of text

        Returns:
        -------
            (List[List[str]]):
                list of acronyms

        Raises:
        -------
            logging.exception:
                Raises the following exception when an empty list is passed
                List is empty. Provide a list of text
            logging.exception:
                Raises the following exception when a string is passed instead of list
                Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list
        """

        # create an empty list to append texts
        final_acronyms_list = []

        try:
            if type(clean_text) is list:

                try:
                    for text in clean_text:
                        # acronyms_list = [word for word in TextProcessing.word_tokenizer([text]) if word.isupper()]
                        acronyms_list = [
                            item
                            for sublist in [word for word in TextProcessing.word_tokenizer([text])]
                            for item in sublist
                            if item.isupper()
                        ]
                        final_acronyms_list.append(acronyms_list)

                except Exception as e:
                    logging.exception(e)
                    print(""" \n List is empty. Provide a list of text. \n""")

        except Exception as e:
            logging.exception(e)
            print(
                """ \n Provide a list of text that needs to be cleaned. Even if it is a single text, pass it as a list \n"""
            )

        return final_acronyms_list
