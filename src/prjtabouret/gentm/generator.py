# SPDX-License-Identifier: GPL-3.0-or-later
"""
---
(c) 2024 David SPORN
---
This is part of prjtabouret -- Documenting the fusemap of the Lattice GAL16V8 PLD and its drop-in replacement MicroChip (Atmel) ATF16V8.

prjtabouret is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

prjtabouret is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
or FITNESS FOR A PARTICULAR PURPOSE.

See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with prjtabouret.
If not, see <https://www.gnu.org/licenses/>. 
---
"""
import json

TARGET_FILENAME = "techmap-gal16v8"


def makeInputPin(name: str) -> str:
    return f"""        pin({name}) {{
            direction: input;
        }}
"""


def pinNameFromInteger(value: int) -> str:
    """Maps a number into a sequence of letters, by replacing each decimal digit by the corresponding letter starting from 'A' mapped to 1."""
    if value <= 0:
        raise ValueError(f"not.strictly.positive:{value}")

    digitToAlpha = ["J", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    current = value
    result = ""
    while current > 0:
        result = digitToAlpha[current % 10] + result
        current = current // 10

    return result


def makeInputPinSet(min: int, max: int):
    """Makes a dictionnary that associate a set of input pin name and their definitions for a cell"""
    result = {}
    for p in range(min, max):
        pname = pinNameFromInteger(p)
        result[pname] = makeInputPin(pname)
    return result


def makeOutputPin(name: str, expr: str):
    return f"""        pin({name}) {{
            direction: output;
            function: "(({expr}))";
        }}
"""


def makeGateCell(
    name: str,
    areaSize: int,
    inputSize: int,
    outputName: str,
    *,
    innerOperator: str = "",
    outerOperator: str = "",
):
    """Makes a gate cell, on the assumption that its output function is f"{outerOperator}({innerOperator.join(input_names)})"""
    if not innerOperator:
        raise ValueError(f"empty:{innerOperator}")
    pinSet = makeInputPinSet(1, 1 + inputSize)
    expr = innerOperator.join(list(pinSet))
    if outerOperator:
        expr = f"{outerOperator}({expr})"

    body = "".join([i for (k, i) in pinSet.items()] + [makeOutputPin(outputName, expr)])

    return f"""    cell({name}) {{
        area: {areaSize};
{body}    }}
"""


def buildAndWriteTechnicalMap(rootFolder: str):
    # 1.
    prologue = """/*
---
SPDX-License-Identifier: CC0-1.0
(c) 2024 David SPORN
---
GAL16v8 Technological map
Version: 0.0.0.dev0

All parameters/attributes/properties are typical, unless stated otherwise
*/
library(gal16v8) {
    cell(GND) {
        area: 0;
        pin(Q) {
            direction: output;
            function: "(0)";
        }
    }
    cell(VCC) {
        area: 0;
        pin(Q) {
            direction: output;
            function: "(1)";
        }
    }
    cell(DFFE) {
        area: 600;
        ff("IQ", "IQN") {
            clocked_on: CLK;
            next_state: D;
        }
        pin(CLK) {
            direction: input;
            clock: true;
        }
        pin(D) {
            direction: input;
        }
        pin(CE) {
            direction: input;
        }
        pin(Q) {
            direction: output;
            function: "IQ";
        }
        pin(QN) {
            direction: output;
            function: "IQN";
        }
        ; // empty statement
    }
    cell(NOT) {
        area: 100;
        pin(A) {
            direction: input;
        }
        pin(QN) {
            direction: output;
            function: "(!A)";
        }
    }
"""

    epilogue = """}
"""

    # -- make OR gates
    orGates = "".join(
        [
            makeGateCell(f"OR{i}", i * 100, i, "Q", innerOperator="+")
            for i in range(2, 9)
        ]
    )

    with open(f"{rootFolder}/{TARGET_FILENAME}.lib", encoding="utf-8", mode="w") as f:
        f.write("\n".join([prologue, orGates, epilogue]))
