# Local imports
from qwilfish.session_builder import register_arbiter

import json

def initialize():
    '''Registers WordleArbiter as a plugin.'''
    register_arbiter(WordleArbiter.PLUGIN_IDENTIFIER, WordleArbiter)

class WordleArbiter:

    PLUGIN_IDENTIFIER = "wordle_arbiter"
    RESULT_FAIL = "FAIL" # Test was executed successfully, but SUT failed somehow
    RESULT_PASS = "PASS" # Test was executed successfully, and SUT withstood 
    RESULT_UNKN = "UNKN" # Test was not executed successfully, result unknown
    RESULT_DRYR = "DRYR" # Test was a dry run, an oracle is requesting holdoff


    def __init__(self):
        pass


    def evaluate(self, reports):
        for report in reports:
            if report.name == "wordle-probe":
                clue_list = json.loads(report.columns["wordle clue"])
                colors = [pair[1] for pair in clue_list]
                if all(color == "green" for color in colors):
                    return WordleArbiter.RESULT_PASS

        return WordleArbiter.RESULT_FAIL


    def dryrun(self):
        return WordleArbiter.RESULT_DRYR


    def unknown(self):
        return WordleArbiter.RESULT_UNKN
