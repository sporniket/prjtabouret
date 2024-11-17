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
    }"""

    epilogue = """}
"""

    with open(f"{rootFolder}/{TARGET_FILENAME}.lib", encoding="utf-8", mode="w") as f:
        f.write("\n".join([prologue, epilogue]))
