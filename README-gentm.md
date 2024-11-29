# gentm -- GENerator of Technology Map

**Content**

1. User manual

## User Manual

### Synopsys

`prjtabouret_gentm [--help] --root <root path>`

`python3 -m prjtabouret.gentm [--help] --root <root path>`

#### Positional arguments

> NONE

#### Options

*  `-h`, `--help`: shows an help message and exits.
*  `--root <root path>` : will generate the technology map into the given folder. The folder -and any necessary parent folders- are created if it does not exist.

### Description

Generate the technology map file of the Lattice GAL16V8 PLD and its drop-in replacement MicroChip (Atmel) ATF16V8.

The generated file is named `techmap-gal16v8.lib`

### Typical invocation

**Given** a source file to format `mysource.s`

```
prjtabouret_gentm --root ./work
```
