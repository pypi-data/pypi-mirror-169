from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import re

class WordsTokenizer:
    """
        Tokenizes text into words
    """
    def __init__(self, tokens=None):
        self.tokens = [] if tokens is None else tokens

    def remove_stopwords(self):
        stops = set(stopwords.words("english")) - set(["not", "too", "so", "very", "but", "no", "nor"])
        self.tokens = [token for token in self.tokens if token not in stops]

    def remove_non_alpha_words(self):
        self.tokens = [token for token in self.tokens if bool(re.fullmatch(r'[A-Za-z]+[_]?[A-Za-z]+', token))]

    def tokenize_text_into_words(self, text):
        if text is None:
            return

        self.tokens = word_tokenize(text)    
