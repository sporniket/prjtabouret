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
import os

FILENAME_LIBERTY = "techmap-gal16v8.lib"


def computeYosysScriptName(name: str) -> str:
    return f"{name}.ys"


def extractNameFromFile(name: str) -> str:
    return os.path.splitext(os.path.basename(name))[0]


def writeYosysScript(sourcename: str, workdir: str):
    name = extractNameFromFile(sourcename)
    scriptName = computeYosysScriptName(name)
    scriptFile = os.path.join(workdir, scriptName)
    with open(scriptFile, encoding="utf-8", mode="w") as f:
        f.write(
            f"""echo on
read_verilog {sourcename}
show -viewer none -format ps -prefix {workdir}/{name}_show
write_json {workdir}/{name}.json
"""
        )
