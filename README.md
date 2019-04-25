## Pentominoes Tester

### Usage

 - Clone the repo or download all files
 - Run `python tester.py PENTOMINOES_EXE` (must be python>=3.6)

**NOTE THAT THIS TESTER IS RUN DIFFERENTLY THAN BEFORE** - instead of supplying your executable as a variable in `tester.py`, the executable is actually now an argument.

When the tester detects an error, it will print a summary and ask if you want to continue or exit. Continuing is default, so just press ENTER instead of typing 'c' if it makes it easier.

### Help

usage: tester.py \[-h\] \[-t TESTCASES\] program

positional arguments:
  program               path to pentominoes solver

optional arguments:
  -h, --help            show this help message and exit
  -t TESTCASES, --testcases TESTCASES
                        custom path to testcases pickle file

### Implementation Notes

If you're too lazy to update Python to >=3.6, you can try to make this program backwards compatible yourself! The only offending line (I think) is where I open a subprocess and include the argument `encoding='utf8'`. If you can figure something else out then you don't need to update Python.

If you happen to still care about Data Structures in tri 2 of your senior year, and if you happen to make this program backwards compatible, please fork this and submit a PR so I can merge it back in. Thanks!

### Report Problems

Solutions were generated from my program, which might not be entirely accurate. If you're finding that your program keeps failing a certain test case and you're sure it's right, let me know and I'll update the solutions if I think your correction is right.
