# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['speech_analytics']

package_data = \
{'': ['*']}

install_requires = \
['happytransformer>=2.4.1,<3.0.0', 'spacy>=3.4.1,<4.0.0']

setup_kwargs = {
    'name': 'speech-analytics',
    'version': '0.1.7',
    'description': '',
    'long_description': "speech-analytics is a simple module for processing speech data collected as\npart of the Calpy project.\n\n# Documentation\n## class ConversationAnalysis\n### Parameters:\n`filename (str)`: The name of a calpy-style data file to analyse.<br>\n\n`model_type (Optional[str])`: The type of spacy model to use in the analysis.\nDefault is `'en_core_web_sm'`.\n\n### Methods:\n`add_analysis(analysis_type: str)`<br>\nAdds the requested type of analysis to the data. Options are:\n- `TOKENIZE`: Tokenize the data in the utterances. The tokens created include raw\n    text, part-of-speech tags, lemma, dependency information, and whether each\n    word is a stop word.\n- `UTTERANCE_LENGTH`: Adds information about the number of words and number of\n    tokens in an utterance.\n- `TURNS`: Combines utterances into turns (i.e. multiple consecutive utterances\n    by the same speaker would be considered one turn).\n- `PREPROCESS`: Runs analysis with TOKENIZE, UTTERANCE_LENGTH, TURNS. Doing so\n    will ensure all other methods work.\n- `REMOVE_AUX_VERBS`: Removes anything classified as an auxiliary verb (based on\n    POS-tagging done in tokenization). If tokenization has not occurred before\n    the removal of aux verbs, add_analysis will be called with the TOKENIZE\n    parameter.\n- `GRAMMAR_CORRECTION`: Adds attempted corrections to grammar. Note that this\n    analysis does not remove the original text (both the original text and)\n    suggested corrections will be available. Utterances will have grammatical\n    corrections suggested, but turns will only have suggested corrections if\n    this is called after add_analysis with TURNS.\n\nThe names of each analysis type are constants provided in the module.<br>\n\n`get_tokens()`<br>\nReturns the raw token information. If no token information is available, this\nmethod will call `add_analysis(TOKENIZE)` in order to derive it.<br>\n\n`get_utterances()`<br>\nReturns the raw utterances. This information will not include\nutterance length unless `add_analysis(UTTERANCE_LENGTH)` is called first.<br>\n\n`get_turns()`<br>\nReturns the raw turns. If turns have not been processed, this method will call\n`add_analysis(TURNS)` first.<br>\n\n`get_turn_info()`<br>\nReturns the raw turn information. If no turn information is available, this\nmethod will call `add_analysis(TURNS)` in order to derive it.<br>\n\n`get_grammar_corrections(by_turn=True)`<br>\nReturns a list of tuples each containing original text and corrected text.\nBy default, this method will return grammar corrections based on turns\n(calling `add_analysis(GRAMMAR_CORRECTION)` where necessary). If `by_turn` is set to False,\ngrammar corrections for utterances will be returned instead.<br>\n\n`get_pos_tags(by_turn=True)`<br>\nReturns the pos tags for each turn (if by_turn is True, else each utterance).\nThe return values is formatted as a list of lists, where each internal list\nconsists of tuples of (token, pos_tag).<br>\n\n`get_turn_length(turn, words=True)`<br>\nReturns the number of words in a turn. If words is set to False, the method instead\nreturns the number of tokens in the turn.<br>\n\n`get_turn_duration(turn)`<br>\nReturns the number of seconds in a turn.<br>\n\n`get_utterance_length(utterance, words=True)`<br>\nReturns the number of words in an utterance. If words is set to False, the method instead\nreturns the number of tokens in the utterance.<br>\n\n`get_utterance_duration(utterance)`<br>\nReturns the number of seconds in an utterance.<br>\n\n`get_pause_length(turn)`<br>\nReturns the total number of seconds between utterances in a turn.\n\n`get_average_turn_length()`<br>\nReturns the average turn length for each speaker, as a dictionary mapping\nspeaker codes to average turn length.<br>\n\n`get_speaker_turns(speaker)`<br>\nReturns a list of all turns taken by the speaker.<br>\n\n`get_speaker_utterances(speaker)`<br>\nReturns a list of all utterances spoken by the speaker.<br>\n\n`get_speaker_names()`<br>\nReturns the names (ids) of all speakers in the conversation.<br>\n",
    'author': 'Ashleigh Richardson',
    'author_email': 'ashleigh.richardson@uqconnect.edu.au',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
