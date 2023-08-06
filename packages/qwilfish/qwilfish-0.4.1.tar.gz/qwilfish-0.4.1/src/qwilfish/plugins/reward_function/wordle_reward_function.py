# Standard lib imports
import math
import json

# Local imports
from qwilfish.session_builder import register_fitness_function

def initialize():
    register_fitness_function(WordleRewarder.PLUGIN_IDENTIFIER,
                              WordleRewarder)

class WordleRewarder:

    PLUGIN_IDENTIFIER = "wordle_rewarder"

    def __init__(self):
        self.score = 0

    def update_score(self, reports):
        for report in reports:
            if report.name == "wordle-probe":
                clue_list = json.loads(report.columns["wordle clue"])
                colors = [pair[1] for pair in clue_list]
                if len(colors) == 5:
                   self.score = colors.count("yellow")
                   self.score += colors.count("green")*5
                else:
                    self.score = 0  # Bad length guess

    def get_current_score(self):
        return self.score
