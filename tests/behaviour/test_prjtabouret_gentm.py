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
import io
import os
import sys

from unittest.mock import patch
from contextlib import redirect_stdout, redirect_stderr

from .utils import initializeTmpWorkspace, assert_that_file_has_expected_content

from prjtabouret.gentm import TechnicalMapGeneratorCli


def test_that_it_generate_techmap_in_target_folder():
    tmp = initializeTmpWorkspace([])

    expected_target_folder = os.path.join(tmp, "techmap")
    expected_techmap_file = os.path.join(expected_target_folder, "techmap-gal16v8.lib")

    ARGS = ["prog", "--root", expected_target_folder]

    with patch.object(sys, "argv", ARGS):
        with redirect_stdout(io.StringIO()) as out:
            with redirect_stderr(io.StringIO()) as err:
                returnCode = TechnicalMapGeneratorCli().run()
        assert returnCode == 0

    assert os.path.isdir(expected_target_folder)
    assert os.path.isfile(expected_techmap_file)

    expected_techmap_content_path = os.path.join(
        "tests", "data.expected", "techmap.lib"
    )
    assert_that_file_has_expected_content(
        expected_techmap_file, expected_techmap_content_path
    )
