'''A fitness function that primarily rewards increases in memory usage.'''

# Standard lib imports
import math

# Local imports
from qwilfish.session_builder import register_fitness_function

def initialize():
    ''' Registers MemChasingFitnessFunc as a plugin.'''
    register_fitness_function(MemChasingFitnessFunc.PLUGIN_IDENTIFIER,
                              MemChasingFitnessFunc)

class MemChasingFitnessFunc:

    PLUGIN_IDENTIFIER = "memory_chasing_fitness_function"

    def __init__(self):
        self.score = 0
        self.base_usage = 0
        self.previous_usage = 0

    def update_score(self, reports):
        # Probably the first time updating the score. Hence, we will only
        # calculate what we assume to be the base/regular usage of the SUT.
        if not self.base_usage:
            for report in reports:
                for k,v in report.columns.items():
                    if k.endswith("mem_usage"):
                        self.base_usage += v
            self.previous_usage = self.base_usage
            return

        curr_mem_usage = 0
        for report in reports:
            for k,v in report.columns.items():
                if k.endswith("mem_usage"):
                    curr_mem_usage += v

        # Score is equal to delta usage between current and previous,
        # normalized by the base usage retrieved during the first run
        mem_diff = math.fabs(curr_mem_usage-self.previous_usage)
        self.score = mem_diff/self.base_usage
        self.previous_usage = curr_mem_usage

    def get_current_score(self):
        return self.score
