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

TARGET_FILENAME = "database-gal16v8"


def initStructRoot(x):
    for n in ["GAL16V8_Registered", "GAL16V8_Complex", "GAL16V8_Simple"]:
        x[n] = {}
        for s in [
            "pins",
            # "specials",
            # "blocks",
            "macrocells",
            "array",
            "globals",
        ]:
            x[n][s] = None


def initGlobals(x, modeName, modeValue):
    x["globals"] = {
        "__doc__": [f"# Global configuration fuses setting for '{modeName}'"],
        "mode": {  # AC1 fuse
            "fuses": [2192, 2193],  # SYN, AC0
            "values": {
                # "registered":2,
                f"{modeName}": modeValue,
                # "simple":1
            },
        },
    }


def initArray(x, mode: str):
    x["array"] = {
        "__doc__": [
            "# Entries of the AND Array",
            "",
            "The AND Array (64 lines of 32 columns) has 16 entries that are injected into it, as well as the inverted value of each entries.",
            "For each entry, the offset in a line of the AND array is given for the normal and the inverted value.",
            "",
            "Each entry value (normal and inverted) is fed by a pad or the feedback of the macrocells.",
            "",
            "The entries are indexed like the pins of a package, in counter-clockwise manner, from 1 to 16, 1 being at the top-left.",
        ]
    }

    # The regular part : entries 1 to 8
    for i in range(0, 8):
        x["array"][f"E{i+1}"] = {
            "offsetNormal": i * 4,
            "offsetInverted": i * 4 + 1,
            "source": f"I{i+2}",
        }

    # The part specific for each mode
    if "registered" == mode:
        for i in range(0, 8):
            j = 8 - i
            x["array"][f"E{i+9}"] = {
                "offsetNormal": j * 4 + 2,
                "offsetInverted": j * 4 + 3,
                "source": f"MC{j}_FB",
            }
    elif "complex" == mode:
        for i in range(0, 8):
            j = 8 - i
            x["array"][f"E{i+9}"] = {
                "offsetNormal": j * 4 + 2,
                "offsetInverted": j * 4 + 3,
                "source": ("I11" if i == 0 else "I1" if i == 7 else f"MC{j}_FB"),
            }
    else:  # simple
        for i in range(0, 8):
            j = 8 - i
            x["array"][f"E{i+9}"] = {
                "offsetNormal": j * 4 + 2,
                "offsetInverted": j * 4 + 3,
                "source": (
                    "I1"
                    if i == 0
                    else (
                        "I11"
                        if i == 7
                        else f"M{j+1}" if i in range(1, 4) else f"M{j-1}"
                    )
                ),
            }


def initMacroCells(x):
    x["macrocells"] = {
        "__doc__": [
            "# Description of each macrocell",
            "",
            "* **net name** : the net name that may be wired to the output of the macrocell.",
            "* **pterm ranges** : for each of the 8 product terms that are inputs of a given macro cell, the range of 32 fuses that control each term.",
            "* **pterm disable** : for each of the 8 product terms that are inputs of a given macro cell, the fuse that disable said product term.",
            "* **configuration fuse** : each cell has a local configuration fuse to change its behaviour.",
            "* **polarity** : fuse to setup whether the output is active high or low, in other word, normal or inverted output.",
        ]
    }
    for i in range(0, 8):
        ptermsOffset = 256 * i
        ptdOffset = 2128 + 8 * i

        x["macrocells"][f"MC{i+1}"] = {
            "net_name": f"M{i+1}",
            "pterm_ranges": {
                f"PT{j+1}": [ptermsOffset + 32 * j, ptermsOffset + 32 * (j + 1)]
                for j in range(0, 8)
            },
            "pterm_disables": {f"PTD{j+1}": ptdOffset + j for j in range(0, 8)},
            "configuration": {
                "fuses": [2120 + i],
                "values": {"registered": 0, "combinatorial": 1},
            },
            "polarity": {
                "fuses": [2048 + i],
                "values": {"active low": 0, "active high": 1},
            },
        }


def initPins(x, *, pin1: str = "I1", pin11: str = "I10"):
    x["pins"] = {
        "__doc__": [
            "# Mapping of physical pin index to a net name",
            "",
            "A **pad** is where the inputs and output pins physically connect to the dye.",
            "For most pins, the pad is linked to a unique net (input or macrocell output).",
            "For pins 1 and 11, depending on the global configuration of the PLD can drive an input net or a special net (clock and output enable), thus their mappings will change between those configurations.",
            "",
            "VCC and GND are dropped as they play no role in the logic.",
        ]
    }
    for pkg in ["DIP20", "PLCC20"]:
        # DIP and PLCC have in fact the same mapping
        # Each physical pin is wired to a given pad
        # Pin 1 and 11 have specific setups
        x["pins"][pkg] = {1: pin1}
        x["pins"][pkg].update({j: f"I{j}" for j in range(2, 10)})
        x["pins"][pkg].update({11: pin11})
        x["pins"][pkg].update({12 + j: f"M{8-j}" for j in range(0, 8)})


def buildAndWriteDatabase(rootFolder: str):
    # 1.
    result = {
        "__licence__": "SPDX-License-Identifier: CC0-1.0",
        "__doc__": [
            "# Database for the GAL16v8 PLD",
            "",
            "Each item describe a global configuration of the device, namely the 'registered' mode, the 'complex' mode and the 'simple' mode.",
        ],
    }
    initStructRoot(result)

    # 2.
    for specs in [
        ["GAL16V8_Registered", "registered", 2],
        ["GAL16V8_Complex", "complex", 3],
        ["GAL16V8_Simple", "simple", 1],
    ]:
        initGlobals(result[specs[0]], specs[1], specs[2])

    # 3.
    for specs in [
        ["GAL16V8_Registered", "registered"],
        ["GAL16V8_Complex", "complex"],
        ["GAL16V8_Simple", "simple"],
    ]:
        initArray(result[specs[0]], specs[1])

    # 4.
    for specs in [["GAL16V8_Registered"], ["GAL16V8_Complex"], ["GAL16V8_Simple"]]:
        initMacroCells(result[specs[0]])

    # 5
    for specs in [
        ["GAL16V8_Registered", "CLK", "OE"],
        ["GAL16V8_Complex"],
        ["GAL16V8_Simple"],
    ]:
        if len(specs) > 1:
            initPins(result[specs[0]], pin1=specs[1], pin11=specs[2])
        else:
            initPins(result[specs[0]])

    with open(f"{rootFolder}/{TARGET_FILENAME}.json", encoding="utf-8", mode="w") as f:
        json.dump(result, f, indent=4)
