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

import os
import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from .generator import buildAndWriteDatabase


class DatabaseGeneratorCli:
    @staticmethod
    def createArgParser() -> ArgumentParser:
        # TODO Rewrite parser as needed
        parser = ArgumentParser(
            prog="python3 -m $$$.pp",
            description="Generate the database file documenting the fusemap of the Lattice GAL16V8 PLD and its drop-in replacement MicroChip (Atmel) ATF16V8.",
            epilog="""---
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
""",
            formatter_class=RawDescriptionHelpFormatter,
            allow_abbrev=False,
        )

        # Add the arguments
        parser.add_argument(
            "--root",
            metavar="<path>",
            type=str,
            help="the path of the folder into which the database will be generated, missing folders in path are created.",
        )

        return parser

    def __init__(self):
        pass

    def run(self):
        try:
            args = DatabaseGeneratorCli.createArgParser().parse_args()
            # TODO other things that may throw a value error
        except ValueError as e:
            print(e, file=sys.stderr)
            return 1
        else:
            if args.root:
                if os.path.exists(args.root):
                    if not os.path.isdir(args.root):
                        print(
                            "ERROR -- specified root folder is not a folder",
                            file=sys.stderr,
                        )
                        return 1
                else:
                    try:
                        os.makedirs(args.root)
                    except:
                        print("ERROR -- cannot create root folder", file=sys.stderr)
                        return 1
            else:
                print(
                    "ERROR -- no root folder specified",
                    file=sys.stderr,
                )
                return 1

            # OK, proceed
            buildAndWriteDatabase(args.root)

            # DONE
            return 0
