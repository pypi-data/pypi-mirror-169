from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from sentiment_pipeline import SentimentPipeline
from nltk import pos_tag

class SentimentAnalysisService():
    def __init__(self):
        self.wordnet_pos = self._create_wordnet_pos()

    def _create_wordnet_pos(self):
        return {
            "J": wordnet.ADJ,
            "V": wordnet.VERB,
            "N": wordnet.NOUN,
            "R": wordnet.ADV
        }

    def run_sentiment_pipeline(self, text):
        pipeline = SentimentPipeline(text)
        return pipeline.run()

    def get_token_with_pos_tag(self, word, tag):
        if tag in self.wordnet_pos:
            return (word, self.wordnet_pos[tag])
        else:
            return (word, None)  

    def get_tokens_with_pos_tags(self, tokens):
        tokes_with_pos = []
        allowed_word_types = ["J", "V", "R", "I", "C", "N"]
        # allowed_word_types = ["J", "C", "R"]

        for f in pos_tag(tokens):
            if f[1][0] in allowed_word_types:
                tokes_with_pos.append(self.get_token_with_pos_tag(f[0], f[1][0]))    
                                    
        return tokes_with_pos

    def lemmatize_word(self, word, tag):
        lemmatizer = WordNetLemmatizer()
        if tag is None:
            return lemmatizer.lemmatize(word)
        
        return lemmatizer.lemmatize(word, pos=tag)   

    def lemmatize_tokens(self, tokens):
        res = ""
        for token in tokens:
            res += self.lemmatize_word(token[0], token[1]) + " "
            
        return res.strip()
