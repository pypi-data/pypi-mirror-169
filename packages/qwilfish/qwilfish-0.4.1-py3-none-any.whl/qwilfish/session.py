# Standard lib imports
import datetime
import logging
import time

# Local imports
from qwilfish.results_db.dataclasses import ResultsDbDatatypes
from qwilfish.results_db.dataclasses import ResultsDbTableDefinition
from qwilfish.results_db.dataclasses import ResultsDbReport

from qwilprobe.client.probe import Probe # TODO make probe wrapper instead

log = logging.getLogger(__name__)

MAIN_TABLE_NAME = "main_results"
CONF_TABLE_NAME = "conf_table"
CASENO_KEY = "caseno"
TIMESTAMP_KEY = "timestamp"
INPUT_KEY = "input"
RESULT_KEY = "result"
FITNESS_KEY = "fitness_score"
CONF_KEY = "conf"

# TODO make these configurable from config file
TAKE_BREAK_TIME = 3 # A few seconds break if needed 
GRAMMAR_UPDATE_CADENCE = 1 # Determines how ofter the grammar is updated

session_main_result_table = ResultsDbTableDefinition(MAIN_TABLE_NAME,
    {
        CASENO_KEY:    ResultsDbDatatypes.INTEGER, # Testcase number
        TIMESTAMP_KEY: ResultsDbDatatypes.TEXT,    # Timestamp for the testcase
        INPUT_KEY :    ResultsDbDatatypes.TEXT,    # Input used in the testcase
        RESULT_KEY:    ResultsDbDatatypes.TEXT,    # Testcase result
        FITNESS_KEY:   ResultsDbDatatypes.REAL,    # Fitness function score
    }
)

session_conf_table = ResultsDbTableDefinition(CONF_TABLE_NAME,
    {
        CONF_KEY:      ResultsDbDatatypes.TEXT     # Configuration params
    }
)

def start_session(fuzzer, courier, results_db, probes, arbiter,
                  fitness_function, conf_params, n_test_cases):
    log.info("Session started at %s", str(datetime.datetime.now()))
    timestamp_start = time.time()
    update_grammar_counter = 0

    # Add columns for the probablistic weights in the grammar to the main table
    for k in fuzzer.get_probabilities().keys():
        new_col = {prob_key_string(k): ResultsDbDatatypes.REAL}
        log.info(f"Adding new column for probability: {new_col}")
        session_main_result_table.columns.update(new_col)

    # Add columns for the mab switches in the grammar to the main table
    for k in fuzzer.get_mab_switches().keys():
        new_col = {mab_key_string(k): ResultsDbDatatypes.INTEGER}
        log.info(f"Adding new column for mab switch: {new_col}")
        session_main_result_table.columns.update(new_col)

    # Initialize the courier
    courier.init()

    # Open a connection to the DB and create the main results table
    results_db.open()
    results_db.create_table(session_main_result_table)

    # Create a table for every probe in use for storing their reports
    if not probes:
        probes = []
    for p in probes:
        probe_info = p.get_probe_info()
        # TODO Probe wrapper class where type conversion is done?
        columns = {}
        for c in probe_info["column_info"]:
            columns[c["column_name"]] = _probe_to_db_datatype(c["column_type"])
        table = ResultsDbTableDefinition(p.get_service_uid(), columns)
        table.columns.update({CASENO_KEY: ResultsDbDatatypes.INTEGER})
        results_db.create_table(table)

    # Save the configuration in the results database
    results_db.create_table(session_conf_table)
    session_conf = ResultsDbReport(CONF_TABLE_NAME, {})
    session_conf.columns.update({CONF_KEY: f"{conf_params}"})
    results_db.write(session_conf)

    for i in range(1, n_test_cases+1):
        # Check that all probes are ready
        is_dryrun = not all(filter(lambda p: p.get_probe_is_ready(), probes))

        # Variable to store the probe reports
        probe_reports = []

        # Set to true if input delivery was attempted and successful
        delivery_ok = False

        # Prepare the main results table for this test case
        main_results = ResultsDbReport(MAIN_TABLE_NAME, {})
        main_results.columns.update({CASENO_KEY: i})
        main_results.columns.update(
            {TIMESTAMP_KEY: f"{str(time.time() - timestamp_start)}"})

        # Add the probabilistic weights used for generation
        for k,v in fuzzer.get_probabilities().items():
            main_results.columns.update({prob_key_string(k): f"{str(v)}"})

        # Add the mab switches used for generation
        for k,v in fuzzer.get_mab_switches().items():
            main_results.columns.update({mab_key_string(k): f"{str(v)}"})

        if is_dryrun: # A probe has requested holdoff, this will be a dry run
            pass
        else: # No probes requested holdoff after last iteration
            fuzz_data, fuzz_metadata = fuzzer.fuzz()
            delivery_ok = courier.deliver(fuzz_data)
            main_results.columns.update({INPUT_KEY: f"{str(fuzz_data)}"})

        for p in probes:
            raw_data = p.get_probe_data()
            report = ResultsDbReport(p.get_service_uid(), raw_data)
            report.columns.update({CASENO_KEY: i})
            probe_reports.append(report)

        if is_dryrun: # This was a dry run
            main_results.columns.update({RESULT_KEY: arbiter.dryrun()})
        elif delivery_ok:
            main_results.columns.update({RESULT_KEY: arbiter.evaluate(probe_reports)})
            if update_grammar_counter == GRAMMAR_UPDATE_CADENCE-1:
                fitness_function.update_score(probe_reports)
                fuzzer.record_score(fitness_function.get_current_score())
                fuzzer.update_mab_switches() # TODO more general API for fuzzer
                update_grammar_counter = 0
            else:
                update_grammar_counter += 1
            score = fitness_function.get_current_score()
            main_results.columns.update({FITNESS_KEY: score})
        else: # Wasn't a dry run but failed to deliver input data to SUT
            log.warning("Couldn't deliver test case input to the target!")
            main_results.columns.update({RESULT_KEY: arbiter.unknown()})

        # Write main results and probe reports to db
        results_db.write(main_results)
        for report in probe_reports:
            results_db.write(report)

        # Dry run or delivery went wrong, take a break before trying again
        if is_dryrun or not delivery_ok:
            msg = f"Taking a break. is_dryrun: {is_dryrun}, "
            msg += f"delivery_ok: {delivery_ok}, test case: {i}"
            log.info(msg)
            time.sleep(TAKE_BREAK_TIME)
            log.info("Woke up from break!")


    courier.destroy()
    results_db.close()
    log.info("# Session ended at %s", str(datetime.datetime.now()))

    return 0

def prob_key_string(k):
    return f"prob.{k}"

def mab_key_string(k):
    return f"mab.{k}"

# TODO make probe wrapper class where this can be handled more cleanly
def _probe_to_db_datatype(probe_type):
    if probe_type == Probe.DATATYPE_INT:
        return ResultsDbDatatypes.INTEGER
    elif probe_type == Probe.DATATYPE_REAL:
        return ResultsDbDatatypes.REAL
    elif probe_type == Probe.DATATYPE_STRING:
        return ResultsDbDatatypes.TEXT
