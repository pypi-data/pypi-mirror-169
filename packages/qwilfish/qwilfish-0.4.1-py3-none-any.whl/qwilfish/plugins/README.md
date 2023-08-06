# How to Add a Plugin
1. Put python module under `src/qwilfish/plugins`
2. Make sure that module contains a method called `initialize` that takes no
arguments
3. `initialize` should register the plugin using the appropriate registration
function in `qwilfish.session_builder`.
    * Registration functions take two arguments, an identifier string and a
    creator function that returns an instance of the plugin.
4. Use the plugin(s) like so:
```
$ qwilfish -C /some/conf/file.yaml
```
where `/some/conf/file.yaml` contains something like:
```
grammar:
  identifier: "my_grammar_plugin_identifier"
courier:
  identifier: "my_courier_plugin_identifier"
```
