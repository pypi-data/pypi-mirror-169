'''Builds a session based on the config it gets'''

# Standard lib imports
import logging

log = logging.getLogger(__name__)

GRAMMAR = "grammar"
COURIER = "courier"
ARBITER = "arbiter"
FITNESS = "fitness"

grammar_build_funcs = {}
courier_build_funcs = {}
arbiter_build_funcs = {}
fitness_build_funcs = {}

build_funcs_lookup = {GRAMMAR: grammar_build_funcs,
                      COURIER: courier_build_funcs,
                      ARBITER: arbiter_build_funcs,
                      FITNESS: fitness_build_funcs}

def register_grammar(identifier, build_func):
    _register(GRAMMAR, identifier, build_func)

def register_courier(identifier, build_func):
    _register(COURIER, identifier, build_func)

def register_arbiter(identifier, build_func):
    _register(ARBITER, identifier, build_func)

def register_fitness_function(identifier, build_func):
    _register(FITNESS, identifier, build_func)

def build_grammar(**kwargs):
    return _build(GRAMMAR, **kwargs)

def build_courier(**kwargs):
    return _build(COURIER, **kwargs)

def build_arbiter(**kwargs):
    return _build(ARBITER, **kwargs)

def build_fitness_function(**kwargs):
    return _build(FITNESS, **kwargs)

def _register(type, identifier, build_func):
    build_funcs = build_funcs_lookup[type]
    if identifier in build_funcs.keys():
        raise ValueError(
            f"Multiple {type} plugins with identifier '{identifier}'")
    build_funcs[identifier] = build_func

def _build(type, **kwargs):
    build_funcs = build_funcs_lookup[type]

    kwargs_copy = kwargs.copy()
    identifier = kwargs_copy.pop("identifier", None)

    if not identifier:
        raise ValueError("No identifier found while configuring plugin!")

    try:
        log.info(f"Building {identifier}")
        build_func = build_funcs[identifier]
        return build_func(**kwargs_copy)
    except KeyError:
        raise ValueError(f"Plugin '{identifier}' has not been registered!")
