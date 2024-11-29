# synth_gal16v8 -- SYNTHetizer for GAL16v8

**Content**

1. User manual

## User Manual

### Synopsys

`prjtabouret_synth_gal16v8 [--help] --workdir <workdir path> <source>`

`python3 -m prjtabouret.synth_gal16v8 [--help] --workdir <workdir path> <source>`

#### Positional arguments

* `<source>` : path to a verilog file to process.

#### Options

*  `-h`, `--help`: shows an help message and exits.
*  `--workdir <workdir path>` : will generate the netlist file into the given folder. The folder -and any necessary parent folders- are created if it does not exist.

### Description

Call yosys to process the given verilog file, in order to get a netlist in json format ready for place and route.

The generated netlist file is named like the source file, with the extension `.json`, e.g. processing the file `test.v` will generate the file `test.json`

### Typical invocation

**Given** a source file to format `my_module.v`

```
prjtabouret_synth_gal16v8 --workdir ./work my_module.v
```
