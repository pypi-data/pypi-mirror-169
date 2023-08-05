from sentiment_amazon_analyzer.text_normalizer_service import SentimentTextNormalizerService
from sentiment_amazon_analyzer.words_tokenizer_service import SentimentWordsTokenizerService
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

class SentimentPipeline():
    """
        Runs text normalizing and word tokenizing processes
    """
    def __init__(self):
        self.wordnet_pos = self._create_wordnet_pos()

    def run(self, text): 
        tokens = self._get_normalized_tokens(text)
        tokens_with_pos_tags = self._get_tokens_with_pos_tags(tokens)
        lemmatized_text = self._lemmatize_tokens(tokens_with_pos_tags)
        print(lemmatized_text)
        return lemmatized_text

    def _get_normalized_tokens(self, text):
        text_normalizer = SentimentTextNormalizerService(text)               
        text_normalizer.convert_to_lower()
        text_normalizer.replace_emoticons()
        text_normalizer.resolve_contractions()
        text_normalizer.remove_html_tags()

        words_tokenizer = SentimentWordsTokenizerService()
        words_tokenizer.tokenize_text_into_words(text_normalizer.text)
        words_tokenizer.remove_stopwords()
        words_tokenizer.remove_non_alpha_words()

        return words_tokenizer.tokens


    def _create_wordnet_pos(self):
        return {
            "J": wordnet.ADJ,
            "V": wordnet.VERB,
            "N": wordnet.NOUN,
            "R": wordnet.ADV
        }

    def _get_token_with_pos_tag(self, word, tag):
        if tag in self.wordnet_pos:
            return (word, self.wordnet_pos[tag])
        else:
            return (word, None)  

    def _get_tokens_with_pos_tags(self, tokens):
        tokes_with_pos = []
        allowed_word_types = ["J", "V", "R", "I", "C", "N"]
        # allowed_word_types = ["J", "C", "R"]

        for f in pos_tag(tokens):
            if f[1][0] in allowed_word_types:
                tokes_with_pos.append(self._get_token_with_pos_tag(f[0], f[1][0]))    
                                    
        return tokes_with_pos

    def _lemmatize_word(self, word, tag):
        lemmatizer = WordNetLemmatizer()
        if tag is None:
            return lemmatizer.lemmatize(word)
        
        return lemmatizer.lemmatize(word, pos=tag)   

    def _lemmatize_tokens(self, tokens):
        res = ""
        for token in tokens:
            res += self._lemmatize_word(token[0], token[1]) + " "
            
        return res.strip()





        
