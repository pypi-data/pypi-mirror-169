# Local imports
from qwilfish.session_builder import register_arbiter

def initialize():
    '''Registers BasicArbiter as a plugin.'''
    register_arbiter(BasicArbiter.PLUGIN_IDENTIFIER, BasicArbiter)

class BasicArbiter:
    '''Decides the outcome of testcases based on oracle reports.
       Fails a testcase if a process is reported as unavailable. Otherwise
       it passes the testcase.'''

    PLUGIN_IDENTIFIER = "basic_arbiter"

    RESULT_FAIL = "FAIL" # Test was executed successfully, but SUT failed somehow
    RESULT_PASS = "PASS" # Test was executed successfully, and SUT withstood 
    RESULT_UNKN = "UNKN" # Test was not executed successfully, result unknown
    RESULT_DRYR = "DRYR" # Test was a dry run, an oracle is requesting holdoff

    def __init__(self):
        pass

    def evaluate(self, reports):
        for report in reports:
            for k,v in report.columns.items():
                if k.endswith("process_state") and not v:
                    return BasicArbiter.RESULT_FAIL

        return BasicArbiter.RESULT_PASS

    def dryrun(self):
        return BasicArbiter.RESULT_DRYR

    def unknown(self):
        return BasicArbiter.RESULT_UNKN
