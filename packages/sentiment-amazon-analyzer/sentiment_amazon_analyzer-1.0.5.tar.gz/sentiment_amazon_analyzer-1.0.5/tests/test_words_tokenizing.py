from sentiment_amazon_analyzer.words_tokenizer_service import SentimentWordsTokenizerService
import pytest

class TestWordsTokenizerService():

    @pytest.mark.parametrize("input, expected", [
      (["hi", "9", "!",  "????"], ["hi"]),
      ([], []),
      (["75", "4rr", "!", "a2d66p"], []),
      (["hi", "how", "are", "you"], ["hi", "how", "are", "you"])
    ])
    def test_should_remove_non_alpha_words(self, input, expected):
        word_tokenizer = SentimentWordsTokenizerService(input)
        word_tokenizer.remove_non_alpha_words()
        assert word_tokenizer.tokens == expected 


    @pytest.mark.parametrize("input, expected", 
    [
        (["are", "am", "the", "an", "good"], ["good"]),
        (["not", "good"], ["not", "good"])
    ])
    def test_should_remove_stopwords(self, input, expected):
        preprocessor = SentimentWordsTokenizerService(input)
        preprocessor.remove_stopwords()
        assert preprocessor.tokens == expected

    @pytest.mark.parametrize("input, expected" , 
    [
        ("Hi, how are you?", ["Hi", ",", "how", "are", "you", "?"]),
        ("I am working on my thesis", ["I", "am", "working", "on", "my", "thesis"]),
        ("Hi, how are you  SMILEY_HAPPY", ["Hi", ",", "how", "are", "you", "SMILEY_HAPPY"])
    ])
    def test_should_tokenize_text_into_words(self, input, expected):
        words_tokenizer = SentimentWordsTokenizerService()
        words_tokenizer.tokenize_text_into_words(input);
        assert words_tokenizer.tokens == expected