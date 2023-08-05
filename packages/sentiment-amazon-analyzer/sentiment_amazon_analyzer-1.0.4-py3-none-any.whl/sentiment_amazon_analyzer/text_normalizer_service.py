import re

class SentimentTextNormalizerService():
    """"
        Normalizes text by 
            converting it to lower case,
            replacing emoticons with their identificators,
            removing html tags,
            resolving contractions
    """
    def __init__(self, text):
        self.text = text
        
    def convert_to_lower(self):
        self.text = None if self.text is None else self.text.lower()

    def replace_emoticons(self):
        smiley_happy = [':-)', ':)', '(:', '(-:', '=)', '(=']
        smiley_sad = [':-(', ':(', '):', ')-:', '=(', ')=']
        smiley_wink = [';-)', ';)', '(;', '(-;']

        if self.text is None:
            return

        for smiley in smiley_happy:
            self.text = self.text.replace(smiley, " SMILEY_HAPPY")
        
        for smiley in smiley_sad:
            self.text = self.text.replace(smiley, " SMILEY_SAD")
        
        for smiley in smiley_wink:
            self.text = self.text.replace(smiley, " SMILEY_WINK")

    def resolve_contractions(self):
        if self.text is None:
            return

        self.text = re.sub(r"won't", "will not", self.text)
        self.text = re.sub(r"wouldn't", "would not", self.text)
        self.text = re.sub(r"couldn't", "could not", self.text)
        self.text = re.sub(r"didn't", "did not", self.text)
        self.text = re.sub(r"n't", " not", self.text)
        self.text = re.sub(r"'d", " would", self.text)
        self.text = re.sub(r"can't", "can not", self.text)
        self.text = re.sub(r"'re", " are", self.text)
        self.text = re.sub(r"'s", " is", self.text)
        self.text = re.sub(r"'ll", " will", self.text)
        self.text = re.sub(r"'t", " not", self.text)
        self.text = re.sub(r"'ve", " have", self.text)
        self.text = re.sub(r"'m", " am", self.text)
        self.text = re.sub(r"'m", " am", self.text)

    def remove_html_tags(self):
        if self.text is None:
            return
            
        tag_re = re.compile(r'<[^>]+>')
        self.text = tag_re.sub('', self.text)     

