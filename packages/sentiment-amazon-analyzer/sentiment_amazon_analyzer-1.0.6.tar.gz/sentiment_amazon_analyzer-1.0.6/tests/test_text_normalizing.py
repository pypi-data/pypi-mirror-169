import pytest
from sentiment_amazon_analyzer.text_normalizer_service import SentimentTextNormalizerService

class TestSentimentTextNormalizerService():

    @pytest.mark.parametrize("input, expected", 
    [
        ("test", "test"),
        ("This is THE test.", "this is the test."),
        (None, None)
    ])
    def test_should_convert_to_lower_case(self, input, expected):
        text_normalizer = SentimentTextNormalizerService(input)
        text_normalizer.convert_to_lower()
        assert text_normalizer.text == expected


    @pytest.mark.parametrize("input, expected", [
        ("Hi, how are you:)", "Hi, how are you SMILEY_HAPPY"),
        ("I feel good ;);) How about you:(", "I feel good  SMILEY_WINK SMILEY_WINK How about you SMILEY_SAD")
    ])
    def test_should_replace_emoticons(self, input, expected):
        text_normalizer = SentimentTextNormalizerService(input)
        text_normalizer.replace_emoticons()
        assert text_normalizer.text == expected

    @pytest.mark.parametrize("input, expected", [
        ("didn't", "did not"),
        ("n't", " not"),
        ("I didn't do anything.", "I did not do anything."),
        ("'d", " would")
    ])
    def test_should_resolve_contractions(self, input, expected):
        text_normalizer = SentimentTextNormalizerService(input)
        text_normalizer.resolve_contractions()
        assert text_normalizer.text == expected

    @pytest.mark.parametrize("input, expected", [
        ("<div>Hi there!</div>", "Hi there!"),
        ("<div id='334' class='btn btn-primary'>hello, how are you?</div>", "hello, how are you?"),
        ("<div><span id='1'>this</span><p> is awesome</p>!<div>", "this is awesome!")
    ])
    def test_should_remove_html_tags(self, input, expected):
        text_normalizer = SentimentTextNormalizerService(input)
        text_normalizer.remove_html_tags()
        assert text_normalizer.text == expected