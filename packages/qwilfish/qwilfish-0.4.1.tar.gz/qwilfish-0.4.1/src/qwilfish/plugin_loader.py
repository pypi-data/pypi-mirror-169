'''Load plugins from qwilfish.plugins'''

# Standard lib imports
import importlib
import pkgutil
import logging
import pathlib
import os.path
import sys

# Local imports
import qwilfish.plugins.arbiter
import qwilfish.plugins.grammar
import qwilfish.plugins.courier
import qwilfish.plugins.reward_function
from qwilfish.constants import QWILFISH_PLUGINSDIR

log = logging.getLogger(__name__)

def _namespace_iterator(package):
    return pkgutil.iter_modules(package.__path__, package.__name__ + ".")

def _import_module(name):
    return importlib.import_module(name)

def _load_plugins_submodule(submodule):
    for _,name,_ in _namespace_iterator(submodule):
        log.info(f"Importing plugin {name}")
        plugin = _import_module(name)
        plugin.initialize() # Loaded module must provide this function!

def _load_homedir_plugins():
    for file in QWILFISH_PLUGINSDIR.rglob("*.py"):
        module_name = os.path.splitext(os.path.basename(file))[0]
        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        module.initialize() # Loaded module must provide this function!

def load_plugins():
    _load_plugins_submodule(qwilfish.plugins.arbiter)
    _load_plugins_submodule(qwilfish.plugins.grammar)
    _load_plugins_submodule(qwilfish.plugins.courier)
    _load_plugins_submodule(qwilfish.plugins.reward_function)

    _load_homedir_plugins()
