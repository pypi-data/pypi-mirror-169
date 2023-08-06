from dataclasses import dataclass
from typing import Optional
import spacy
import json
from pprint import pprint

@dataclass
class Item:
    confidence: float
    content: str

@dataclass
class Word(Item):
    start_time: float
    end_time: float

@dataclass
class Punctuation(Item):
    pass

@dataclass
class Token:
    text: str
    upos: str
    pos: str
    lemma: str
    dep: str
    # shape: str
    # is_alpha: bool
    is_stop: bool

@dataclass
class Utterance:
    speaker_label: str
    start_time: float
    end_time: float
    full_text: str
    items: list[Item]
    tokens: Optional[list[Token]] = None
    num_words: Optional[int] = None
    num_tokens: Optional[int] = None
    grammar_corrected: Optional[str] = None

    def __repr__(self):
        return f"{self.speaker_label}: {self.full_text}"

@dataclass
class Turn:
    speaker_label: str
    utterances: list[Utterance]
    full_text: str
    grammar_corrected: Optional[str] = None

class BaseModel:
    def __init__(self, model_type: Optional[str] ='en_core_web_sm'):
        """ Construct a new model. If model_type is supplied, the requested
            model is loaded from spacy. Otherwise a new model is created.
        """
        # TODO: handle model_type of None
        self._nlp = spacy.load(model_type)
        self._analyses = {}
    
    def generate_docs(self, utterances: list[Utterance]):
        return self._nlp.pipe([utterance.full_text for utterance in utterances])

    def add_analysis(self, analysis_type: str):
        raise NotImplementedError('Subclasses must enable analyses')

TOKENIZE = 'tokenize'
UTTERANCE_LENGTH = 'utterance_length'
TURNS = 'turns'
REMOVE_AUX_VERBS = 'remove_aux'
GRAMMAR_CORRECTION = 'grammar_correction'
FULL_UTTERANCES = 'full'
TOKENS = 'tokens'
ITEMS = 'items'
TEXT = 'text'

def process_utterances(segments, speakers):
    # TODO: is it assumed the speaker label segments are broken down the same way as
    # text segments?
    utterances = []
    for speaker, segment in zip(speakers, segments):
        start, end = float(speaker.get('start_time')), float(speaker.get('end_time'))
        segment_start, segment_end = float(segment.get('start_time')), float(segment.get('end_time'))
        # Ensure the speaker and segment start and end roughly align: TODO make flexible within eta
        if segment_start != start or end != segment_end:
            print('Unaligned segments')
            return

        speaker_lbl = speaker.get('speaker_label')
        # TODO: just take first utterance? Looks like some have multiple alternatives
        text = segment.get('alternatives')[0]
        full_text = text['transcript']

        items = []

        for item in text['items']:
            item_type = item.get('type')
            confidence, content = float(item['confidence']), item['content']
            if item_type == 'punctuation':
                items.append(Punctuation(confidence, content))
            else:
                items.append(Word(
                    confidence=confidence,
                    content=content,
                    start_time=float(item.get('start_time')),
                    end_time=float(item.get('end_time'))
                ))

        utterances.append(Utterance(
            speaker_label=speaker_lbl,
            start_time=start,
            end_time=end,
            full_text=full_text,
            items=items
        ))
    return utterances

def process_raw_data(data):
    # data here is just the 'results' value of the loaded file
    segments = data.get('segments')
    speakers = data.get('speaker_labels').get('segments')
    utterances = process_utterances(segments, speakers)
    return utterances

def load_file(filename):
    with open(filename, 'r') as file:
        contents = json.loads(file.readlines()[0])
    return contents

class ConversationAnalysis(BaseModel):
    def __init__(self, filename: str, model_type: Optional[str] ='en_core_web_sm'):
        """ Construct a new model. If model_type is supplied, the requested
            model is loaded from spacy. Otherwise a new model is created.
        """
        # TODO: handle model_type of None
        super().__init__(model_type=model_type)
        self._utterances = process_raw_data(load_file(filename).get('results'))
        self._turns = []
        self.load_data()
    
    def _set_utterances(self, utterances):
        # this should only be for testing, don't make available
        self._utterances = utterances

    def load_data(self):
        self._docs = self.generate_docs(self._utterances)

    def add_analysis(self, analysis_type: str):
        self.load_data() # Reload data to reset self._docs generator
        if analysis_type == TOKENIZE:
            for doc_num, doc in enumerate(self._docs):
                self._utterances[doc_num].tokens = [Token(token.text, token.pos_, token.tag_, token.lemma_, token.dep_, token.is_stop) for token in doc]
        elif analysis_type == UTTERANCE_LENGTH:
            for doc_num, doc in enumerate(self._docs):
                self._utterances[doc_num].num_tokens = len(doc)
                self._utterances[doc_num].num_words = len([item for item in self._utterances[doc_num].items if isinstance(item, Word)])
        elif analysis_type == TURNS:
            for utterance in self._utterances:
                if not self._turns or self._turns[-1].speaker_label != utterance.speaker_label:
                    self._turns.append(Turn(utterance.speaker_label, [utterance], utterance.full_text))
                else:
                    self._turns[-1].utterances.append(utterance)
                    self._turns[-1].full_text += ' ' + utterance.full_text

        elif analysis_type == REMOVE_AUX_VERBS:
            for utterance in self._utterances:
                for j, token in enumerate(utterance.tokens):
                    if token.upos == 'AUX':
                        item = utterance.tokens.pop(j)
                        print('removing', item)
                utterance.full_text = ' '.join([token.text for token in utterance.tokens])
        elif analysis_type == GRAMMAR_CORRECTION:
            self.suggest_grammatical_corrections()

    def get_utterances(self, info=FULL_UTTERANCES):
        if info == FULL_UTTERANCES:
            return self._utterances
        elif info == TOKENS:
            return [utterance.tokens for utterance in self._utterances]
        elif info == TEXT:
            return [utterance.full_text for utterance in self._utterances]
        elif info == ITEMS:
            return [utterance.items for utterance in self._utterances]

    def get_turns(self):
        turns = []
        for utterance in self._utterances:
            if turns and turns[-1]['speaker_label'] == utterance.speaker_label:
                turns[-1]['utterances'] += [utterance]
            else:
                turns.append({
                    'speaker_label': utterance.speaker_label,
                    'utterances': [utterance]
                })
        for turn in turns:
            turn['words_in_turn'] = sum([utterance.num_words for utterance in turn['utterances']])
            turn['tokens_in_turn'] = sum([utterance.num_tokens for utterance in turn['utterances']])
        return turns
    
    def suggest_grammatical_corrections(self, num_beams=5, min_length=1):
        from happytransformer import HappyTextToText, TTSettings
        self._happy_tt = HappyTextToText("T5", "vennify/t5-base-grammar-correction")
        self._args = TTSettings(num_beams=num_beams, min_length=min_length)

        for turn in self._turns:
            result = self._happy_tt.generate_text("grammar: " + turn.full_text, args=self._args)
            turn.grammar_corrected = result.text

        for utterance in self._utterances:
            result = self._happy_tt.generate_text("grammar: " + utterance.full_text, args=self._args)
            utterance.grammar_corrected = result.text

    def get_grammar_corrections(self, by_turn=True):
        txt = 'turn' if by_turn else 'utterance'
        print('Grammar corrections by ' + txt)

        to_analyse = self._turns if by_turn else self._utterances
        for i, item in enumerate(to_analyse):
            print(txt, str(i) + '\n')
            print('Original text: ', item.full_text)
            print('Corrected text:', item.grammar_corrected)
            print('\n' + '-' * 25)

if __name__ == '__main__':
    # model = GrammaticalAnalysis('./testData/test1.json')
    # model.analyse()
    fake_data = [
        Utterance('lbl1', 0.0, 0.5, 'Hello how you going', items=None, tokens = None),
        Utterance('lbl2', 0.5, 1.0, 'ok how you?', items=None, tokens = None),
        Utterance('lbl1', 1.0, 2.0, 'Not too bad, thanks!', items=None, tokens = None)
    ]
    model = ConversationAnalysis('./testData/test1.json')
    # model._set_utterances(fake_data)
    model.add_analysis(TURNS)
    model.add_analysis(GRAMMAR_CORRECTION)
    model.get_grammar_corrections()
    print()
    model.get_grammar_corrections(by_turn = False)
