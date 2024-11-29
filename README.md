# prjtabouret-by-sporniket

![PyPI - Version](https://img.shields.io/pypi/v/prjtabouret-by-sporniket)
![PyPI - License](https://img.shields.io/pypi/l/prjtabouret-by-sporniket)


> [WARNING] Please read carefully this note before using this project. It contains important facts.

Content

1. What is **prjtabouret-by-sporniket**, and when to use it ?
2. What should you know before using **prjtabouret-by-sporniket** ?
3. How to use **prjtabouret-by-sporniket** ?
4. Known issues
5. Miscellanous

## 1. What is **prjtabouret-by-sporniket**, and when to use it ?

**prjtabouret-by-sporniket** is a project for documenting the fusemap of the Lattice GAL16V8 PLD and its drop-in replacement MicroChip (Atmel) ATF16V8. It also aims at using yosys and nextpnr in order to generate a JED file from a yosys supported input file (for now verilog only, rtlil is on the roadmap).

**prjtabouret-by-sporniket** is very inspired by [prjbureau by whitequark](https://github.com/whitequark/prjbureau).

### What's new in v0.0.1

Initial release. It provides the following scripts : 

* `gendb` : generate a json database of the Lattice GAL16V8 PLD.
* `gentm` : generate a liberty file to be used by yosys for its technology mapping step.
* `synth_gal16v8` : a script that calls yosys to process an input file ; _this is just a Proof Of Concept_, for now it just read the given verilog and directly generate a dot view and the netlist.

### Licence

 **prjtabouret-by-sporniket** is free software: you can redistribute it and/or modify it under the terms of the
 GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
 option) any later version.

 **prjtabouret-by-sporniket** is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
 more details.

 You should have received a copy of the GNU General Public License along with **prjtabouret-by-sporniket**.
 If not, see http://www.gnu.org/licenses/ .

## 2. What should you know before using **prjtabouret-by-sporniket** ?

**prjtabouret-by-sporniket** is written in [Python](http://python.org) language. It requires [Yosys](https://yosyshq.net/) (and later [nextpnr](https://github.com/YosysHQ/nextpnr)).

> Do not use **prjtabouret-by-sporniket** if this project is not suitable for your project

## 3. How to use **prjtabouret-by-sporniket** ?

### Requirements

* Python 3.9 or later versions.
* Required command : `pipx`, see [pipx homepage](https://pipx.pypa.io/stable/).
* Required python dependency manager `pdm` : `pipx install pdm`.
* Required external command : `yosys`, see [yosys manual](https://yosyshq.net/)

### From source

To get the latest available code, one must clone the git repository, build and install to the maven local repository.

	git clone https://github.com/sporniket/prjtabouret.git
	cd prjtabouret
	pdm build
  pipx install dist/prjtabouret_by_sporniket-<version>-py3-none-any.whl

### From Pypi
Add any of the following dependencies that are appropriate to your project.

```
pipx install prjtabouret_by_sporniket
```


## 4. Known issues
See the [project issues](https://github.com/sporniket/prjtabouret/issues) page.

## 5. Miscellanous

### Report issues
Use the [project issues](https://github.com/sporniket/prjtabouret/issues) page.
