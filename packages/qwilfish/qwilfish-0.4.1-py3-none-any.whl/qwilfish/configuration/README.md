# Advanced Configuration
## Session Configuration
The fuzzing session can be configured by invoking qwilfish with the `-C` flag
followed by the path to a YAML configuration file. No schema exists for this
file yet, but currently it only supports two keys: `grammar` and `courier`.

### Configuring the grammar
The grammar used for generating fuzzy data can be specified using the `grammar`
key. The corresponding value should be a single key-value pair with the key
`identifier` and a value corresponding to a plugin identifier. For example:
```
grammar:
  identifier: "lldp_grammar"
```
For more info on plugins see [the plugins README](../plugins/README.md)

### Configuring the courier
The way that the test data is delivered to the SUT can be configured using the
`courier` key. The corresponding value should be a list of key-value pairs with
configuration for the courier. The only mandatory key is the `identifier` key
whose value should be a plugin identifier, for example:
```
courier:
  identifier: "raw_socket_courier"
  interface: "lo"
```
For more info on plugins see [the plugins README](../plugins/README.md)

### Logging Configuration
Detailed logging configuration for the `logging` standard Python module can be
provided with a "logging" section in the configuration file pointed out with
the `-C` flag. The section should follow
[this dict schema](https://docs.python.org/3.10/library/logging.config.html#logging-config-dictschema).
