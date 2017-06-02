import logging
from .replace_from_dictionary import replace_from_dictionary
from .separated_parenthesis import separated_parenthesis
from .token_replacement import token_replacement
from .decaps_text import decaps_text
from .pos_tokenizer import pos_tokenizer
from .dedash import dedash
from .unidecoder import unidecoder
from .titlecaps import titlecaps
from .replace_acronyms import replace_acronyms
from .identify_parenthetical_phrases import identify_parenthetical_phrases
from .seperate_reference import seperate_reference

__all__ = [
    'separated_parenthesis',
    'token_replacement',
    'decaps_text',
    'dedash',
    'pos_tokenizer',
    'titlecaps',
    'replace_from_dictionary',
    'identify_parenthetical_phrases',
    'unidecoder',
    'replace_acronyms',
    'seperate_reference'
]

logger = logging.getLogger(__name__)
logging.basicConfig()
