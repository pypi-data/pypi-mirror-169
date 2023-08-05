from sentiment_amazon_analyzer.sentiment_pipeline import SentimentPipeline
import pytest

# odraditi word tokenize sa hi!
class TestSentimentPipeline():    

    @pytest.mark.parametrize("input, expected", [
        (
            """
                This tv is awesome :) 
                I like lg tvs, because of the quality. 
                I've got 9 of them. Nice product!
            """, 
            "tv awesome SMILEY_HAPPY like lg tvs quality get nice product"
        ),
        ( "and", "" ), 
        ( "011 how are you", "" ), 
        ( ",", "" ),
        ( "But, it's not working:(", "but not work SMILEY_SAD" ),
        ( None, "" )
    ])
    def test_sentiment_pipeline_run(self, input, expected):
        pipeline = SentimentPipeline()
        result = pipeline.run(input)
        assert result == expected

    @pytest.mark.parametrize("input, expected", [
        (
            """
                This tv is awesome :) 
                I like lg tvs, because of the quality. 
                I've got 9 of them. Nice product!
            """, 
            [
                "tv", "awesome", "SMILEY_HAPPY", "like", "lg", "tvs",
                "quality", "got", "nice", "product"
            ]
        ),
        ( "and", [] ), 
        ( "011 how are you", [] ), 
        ( ",", [] ),
        ("But, it's not working:(", ["but", "not", "working", "SMILEY_SAD"]),
        (None, [])
    ])
    def test_sentiment_pipeline_get_normalized_tokens(self, input, expected):
        pipeline = SentimentPipeline()
        result = pipeline._get_normalized_tokens(input)
        assert result == expected

    @pytest.mark.parametrize("input, expected", [
        (
            """
                This tv is awesome :) 
                I like lg tvs, because of the quality. 
                I've got 9 of them. Nice product!
            """, 
            [
                "tv", "awesome", "SMILEY_HAPPY", "like", "lg", "tvs",
                "quality", "got", "nice", "product"
            ]
        ),
        ( "and", [] ), 
        ( "011 how are you", [] ), 
        ( ",", [] ),
        ("But, it's not working:(", ["but", "not", "working", "SMILEY_SAD"]),
        (None, [])
    ])
    def test_sentiment_pipeline_get_normalized_tokens(self, input, expected):
        pipeline = SentimentPipeline()
        result = pipeline._get_normalized_tokens(input)
        assert result == expected







