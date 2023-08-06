# Standard lib imports
import importlib.resources
import logging
from logging.config import dictConfig
import os
import os.path

# Third-party imports
import yaml
from qwilprobe.client.probe import Probe

# Local imports
from qwilfish.qwilfuzzer import QwilFuzzer
from qwilfish.session import start_session
from qwilfish.parser import parse_arguments
from qwilfish.results_db.database import ResultsDb
import qwilfish.configuration # Conf files have their own subpackage
from qwilfish import session_builder
from qwilfish import plugin_loader
from qwilfish.constants import (
    QWILFISH_DEFAULT_CONFIG_FILE,
    QWILFISH_CONFIGDIR,
    QWILFISH_GRAMMARDIR,
    QWILFISH_ARBITERDIR,
    QWILFISH_COURIERDIR,
    QWILFISH_REWARDFUNCDIR
)

def main():
    args = parse_arguments()

    # Don't run any campaign, just create ~/.qwilfish
    if args.init_home_dir:
        _create_homedir()
        return 0

    # Load plugins
    plugin_loader.load_plugins()

    conf, conf_filename = _read_configuration(args.config_file)

    log_conf = conf.get("logging")
    if args.debug:
        log_conf.get("handlers").get("console").update({"level": "DEBUG"})
    log = logging.getLogger(__name__)
    dictConfig(log_conf)
    log.info(f"Read configuration file: {conf_filename}")


    # TODO Read conf into a dict
    session_conf = conf.get("campaign")
    log.debug(f"Session configuration read: {session_conf}")

    # Session conf params will be stored as a string for documentation purposes
    conf_to_db = {}
    conf_to_db.update({"from_file": session_conf.copy()})
    conf_to_db.update({"from_cli": vars(args)})
    conf_to_db = yaml.dump(conf_to_db)

    # Choose a grammar to generate packets from
    grammar = session_builder.build_grammar(**session_conf["grammar"])

    # Create the fuzzer engine from the grammar
    fuzzer = QwilFuzzer(grammar, unguided_fuzzing=args.unguided)

    # Create a courier that delivers the fuzzy input by sending it on a socket
    courier = session_builder.build_courier(**session_conf["courier"])

    # Create the database for logging the test results, if enabled
    results_db = ResultsDb(args.outfile, args.dont_store_results)

    # Read probe configurations
    probes = []
    for p in session_conf.get("probes", []):
        probes.append(Probe(service_uid=p["uid"],
                      address=p["address"],
                      port=p["port"]))

    arbiter = session_builder.build_arbiter(**session_conf["arbiter"])

    fitness_function = session_builder.build_fitness_function(
        **session_conf["fitness_function"])

    return start_session(fuzzer,
                         courier,
                         results_db,
                         probes,
                         arbiter,
                         fitness_function,
                         conf_to_db,
                         args.count)


def _read_configuration(filename):
    if filename:
       config_file = filename
    else:
        config_file = QWILFISH_DEFAULT_CONFIG_FILE

    # Used to look in the current dir, also used when filename is absolute
    config_file_cur = config_file
    # Used to look for conf in the .qwilfish folder under user's homedir
    config_file_home = os.path.join(QWILFISH_CONFIGDIR, config_file)
    # Used to look for conf where the module is installed
    tmp_path = importlib.resources.files(
        qwilfish.configuration).joinpath(config_file)
    with importlib.resources.as_file(tmp_path) as path:
        config_file_module = path

    # Prioritize what config file to select, if multiple possibilities
    if os.path.isfile(config_file_cur):
        selected_config = config_file_cur
    elif os.path.isfile(config_file_home):
        selected_config = config_file_home
    elif os.path.isfile(config_file_module):
        selected_config = config_file_module
    else:
        raise ValueError(f"Config file {config_file} not found!")

    with open(selected_config) as f:
       configuration = yaml.safe_load(f)

    return configuration, selected_config

def _create_homedir():
    dirs = [QWILFISH_CONFIGDIR,
            QWILFISH_GRAMMARDIR,
            QWILFISH_ARBITERDIR,
            QWILFISH_COURIERDIR,
            QWILFISH_REWARDFUNCDIR]
    for d in dirs:
        try:
            os.makedirs(d)
        except FileExistsError as e:
            if not os.path.isdir(d):
                raise Exception(f"Found non-directory file: {d}") from e
