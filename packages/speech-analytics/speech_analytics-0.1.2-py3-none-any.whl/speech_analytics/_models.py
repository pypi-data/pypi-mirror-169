import spacy

class Analysis:
    def __init__(self, model_type = 'en_core_web_sm'):
        self._nlp = spacy.load(model_type)
