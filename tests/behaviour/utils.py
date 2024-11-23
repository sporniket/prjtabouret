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
import filecmp
import io
import os
import shutil
import sys
import time

from contextlib import redirect_stdout
from typing import List
from unittest.mock import patch


def makeTmpDirOrDie(suffix: str = None) -> str:
    newdir = os.path.join(".", f"tmp.{suffix}" if suffix != None else "tmp")
    if os.path.exists(newdir):
        if os.path.isdir(newdir):
            return newdir
        raise (ResourceWarning(f"{newdir} is not a directory"))
    os.mkdir(newdir)
    return newdir


def initializeTmpWorkspace(files: List[str]) -> str:
    tmp_dir = makeTmpDirOrDie(f"test_{time.time()}")
    for file in files:
        if file[-2:].upper() == ",A":
            file = file[:-2]
        shutil.copy(file, tmp_dir)
    return tmp_dir


def assert_that_file_has_expected_content(
    pathActual: str, pathExpected: str, substitutionMap: dict[str, str] = None
):
    if substitutionMap:
        with open(pathActual, "rt") as fact:
            actualBody = fact.read()
        with open(pathExpected, "rt") as fexp:
            expectedBody = fexp.read()
        for k, v in substitutionMap.items():
            expectedBody = expectedBody.replace(k, v)
        assert len(actualBody) > 0
        assert actualBody == expectedBody
    else:
        assert filecmp.cmp(pathActual, pathExpected, shallow=False)
