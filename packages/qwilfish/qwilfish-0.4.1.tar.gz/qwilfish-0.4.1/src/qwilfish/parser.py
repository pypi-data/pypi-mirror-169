# Standard library imports
import argparse

DEFAULT_GRPC_ADDRESS = "127.0.0.1"
DEFAULT_GRPC_PORT = 54545

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--debug",
                        dest="debug",
                        help="Override logging conf, log DEBUG to stderr",
                        action="store_true")

    parser.add_argument("-I", "--init-home-directory",
                        dest="init_home_dir",
                        help="create folder for plugins and conf under $HOME",
                        action="store_true")

    parser.add_argument("-C", "--config-file",
                        dest="config_file",
                        help="Specify configuration file for the campaign",
                        default=None,
                        type=str)

    parser.add_argument("-c", "--count",
                        dest="count",
                        help="number of fuzzed packets to transmit",
                        type=int,
                        default=1)

    parser.add_argument("-u", "--unguided",
                        dest="unguided",
                        help="unguided fuzzing, fixed grammar probabilities",
                        action="store_true")

    results_group = parser.add_mutually_exclusive_group()

    results_group.add_argument("-o", "--outfile",
                               dest="outfile",
                               help="file for storing test results",
                               type=str,
                               default="")

    results_group.add_argument("-n", "--no-results-file",
                               dest="dont_store_results",
                               help="don't store test results on disk",
                               action="store_true")

    return parser.parse_args()
