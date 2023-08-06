'''
Constants used within the package
'''

from pathlib import Path

DEFAULT_START_SYMBOL = "<start>"


QWILFISH_HOMEDIR = Path.home().joinpath(".qwilfish")
QWILFISH_CONFIGDIR = QWILFISH_HOMEDIR.joinpath("config")
QWILFISH_DEFAULT_CONFIG_FILE = "default.yaml"
QWILFISH_PLUGINSDIR = QWILFISH_HOMEDIR.joinpath("plugins")
QWILFISH_GRAMMARDIR = QWILFISH_PLUGINSDIR.joinpath("grammar")
QWILFISH_ARBITERDIR = QWILFISH_PLUGINSDIR.joinpath("arbiter")
QWILFISH_COURIERDIR = QWILFISH_PLUGINSDIR.joinpath("courier")
QWILFISH_REWARDFUNCDIR = QWILFISH_PLUGINSDIR.joinpath("reward_function")
