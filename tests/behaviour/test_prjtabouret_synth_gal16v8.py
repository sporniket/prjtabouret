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
import json
import os
import re
import sys

from unittest.mock import patch
from contextlib import redirect_stdout, redirect_stderr

from .utils import initializeTmpWorkspace, assert_that_file_has_expected_content

from prjtabouret.synth_gal16v8 import SynthetizerGal16v8Cli

REFERENCE_DIR = os.path.join("tests", "data")


def test_that_it_uses_default_topmodule_value_when_not_specified():
    tmp = initializeTmpWorkspace([os.path.join(REFERENCE_DIR, "test_top.v")])

    source_file = os.path.join(tmp, "test_top.v")
    expected_target_folder = os.path.join(tmp, "build")
    expected_techmap_file = os.path.join(expected_target_folder, "test_top.ys")

    ARGS = ["prog", "--workdir", expected_target_folder, source_file]

    with patch.object(sys, "argv", ARGS):
        with redirect_stdout(io.StringIO()) as out:
            with redirect_stderr(io.StringIO()) as err:
                returnCode = SynthetizerGal16v8Cli().run()
        assert err.read() == ""
        assert returnCode == 0

    assert os.path.isdir(expected_target_folder)
    assert os.path.isfile(expected_techmap_file)

    expected_techmap_content_path = os.path.join(
        "tests", "data.expected", "test_top.ys"
    )
    assert_that_file_has_expected_content(
        expected_techmap_file,
        expected_techmap_content_path,
        {"@@@TMP@@@": tmp, "@@@TOP@@@": "top"},
    )

    # netlist file
    expected_netlist_file = os.path.join(expected_target_folder, "test_top.json")
    assert os.path.isfile(expected_netlist_file)
    with open(expected_netlist_file) as netlistSource:
        netlist = json.load(netlistSource)
        creator = netlist["creator"]

        assert len(creator) > 6  # more than "yosys "
        assert creator[:6] == "Yosys "
        assert re.match("Yosys [0-9.]+.*", creator) is not None


def test_that_it_generate_techmap_and_netlist_in_target_folder():
    tmp = initializeTmpWorkspace([os.path.join(REFERENCE_DIR, "test.v")])

    source_file = os.path.join(tmp, "test.v")
    expected_target_folder = os.path.join(tmp, "build")
    expected_techmap_file = os.path.join(expected_target_folder, "test.ys")

    ARGS = [
        "prog",
        "--workdir",
        expected_target_folder,
        "--topmodule",
        "test__GAL16V8_registered__DIP",
        source_file,
    ]

    with patch.object(sys, "argv", ARGS):
        with redirect_stdout(io.StringIO()) as out:
            with redirect_stderr(io.StringIO()) as err:
                returnCode = SynthetizerGal16v8Cli().run()
        assert err.read() == ""
        assert returnCode == 0

    assert os.path.isdir(expected_target_folder)
    assert os.path.isfile(expected_techmap_file)

    expected_techmap_content_path = os.path.join("tests", "data.expected", "test.ys")
    assert_that_file_has_expected_content(
        expected_techmap_file,
        expected_techmap_content_path,
        {"@@@TMP@@@": tmp, "@@@TOP@@@": "test__GAL16V8_registered__DIP"},
    )

    # netlist file
    expected_netlist_file = os.path.join(expected_target_folder, "test.json")
    assert os.path.isfile(expected_netlist_file)
    with open(expected_netlist_file) as netlistSource:
        netlist = json.load(netlistSource)
        creator = netlist["creator"]

        assert len(creator) > 6  # more than "yosys "
        assert creator[:6] == "Yosys "
        assert re.match("Yosys [0-9.]+.*", creator) is not None
