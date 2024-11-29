# gendb -- GENerator of DataBase

**Content**

1. User manual
2. Database schema

## User Manual

### Synopsys

`prjtabouret_gendb [--help] [--root <root path>]`

`python3 -m prjtabouret.gendb [--help] [--root <root path>]`

#### Positional arguments

> NONE

#### Options

*  `-h`, `--help`: shows an help message and exits.
*  `--root <root path>` : will generate the database into the given folder. The folder -and any necessary parent folders- are created if it does not exist.

### Description

Generate the database file documenting the fusemap of the Lattice GAL16V8 PLD and its drop-in replacement MicroChip (Atmel) ATF16V8.

### Typical invocation

**Given** a source file to format `mysource.s`

```
prjtabouret_gendb --root ./work
```

## Database schema

The database is a JSON representation.

Some nodes have **metadata** fields. Metadata fields name are surrounded by double underscore (`__`). For now there is : 
* `__version__` (root node only) : a semantic version number (e.g. like version numbering described in [PEP440](https://peps.python.org/pep-0440/))
* `__licence__` (root node only) : a licence declaration, a SPDX expression can be formally specified by starting the value with `SPDX-License-Identifier: `, e.g. `SPDX-License-Identifier: CC0-1.0`
* `__comment__` (any node) : an array of strings using [the markdown syntax](https://daringfireball.net/projects/markdown/).

**Metadata fields are _reserved_**

When one wants to enrich metadata with one's own metadata name, one MUST use **user metadata** fields. User metadata fields are surrounded by triple underscore (`___`), e.g. `___my_veryOwn_METADATA___`.


The overall hierarchy of nodes is as following : 

```
<root>
    <device_setup>
        pins
            <package>
        macrocells
            <cell>
        array
            <entry>
        globals
            mode
```

The generated database embeds enough comments to understand more how data is structured and what it describe.
