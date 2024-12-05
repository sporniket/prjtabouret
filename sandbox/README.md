# Experimenting with yosys

## How to use

* Create a `build`
* For a given `*.ys` file, e.g. `test-cnt.ys`, run yosys with the `-s` switch, e.g. : `yosys -s test-cnt.ys`
* The visualisations of the netlist are created in `dot` and `svg` format.

## List of experiments

* `test-comb` : to see how basic combinations (and, or ,xor, and some inversion) are processed.
* `test-cnt` : to see how a simple counter (add 1 for each clock) is processed
* `test-tri` : to see how a tri-state buffer is processed.

## Principles

* The script force to use only AND, OR and NOT gates
* The script instruct to recognize tri-state buffers
* The script instruct to separate multi-bits wire/registers into separate net