# Local imports
from qwilfish.session_builder import register_grammar
from qwilfish.constants import DEFAULT_START_SYMBOL
from qwilfish.grammar import opts

PLUGIN_IDENTIFIER = "wordle_grammar"

def initialize():
    '''Will be called by the plugin loader.'''
    register_grammar(PLUGIN_IDENTIFIER, create)

def create():
    return OTHER_GRAMMAR.copy()


OTHER_GRAMMAR = {
    DEFAULT_START_SYMBOL:
        ["1<letter><letter><letter><letter><letter>"],
    "<letter>":
        [("a", opts(mab=1)),
         ("b", opts(mab=1)),
         ("c", opts(mab=1)),
         ("d", opts(mab=1)),
         ("e", opts(mab=1)),
         ("f", opts(mab=1)),
         ("g", opts(mab=1)),
         ("h", opts(mab=1)),
         ("i", opts(mab=1)),
         ("j", opts(mab=1)),
         ("k", opts(mab=1)),
         ("l", opts(mab=1)),
         ("m", opts(mab=1)),
         ("n", opts(mab=1)),
         ("o", opts(mab=1)),
         ("p", opts(mab=1)),
         ("q", opts(mab=1)),
         ("r", opts(mab=1)),
         ("s", opts(mab=1)),
         ("t", opts(mab=1)),
         ("u", opts(mab=1)),
         ("v", opts(mab=1)),
         ("w", opts(mab=1)),
         ("x", opts(mab=1)),
         ("y", opts(mab=1)),
         ("z", opts(mab=1)),
        ]
}
