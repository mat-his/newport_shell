import argparse

from newport_shell.console import ConsoleManager
from newport_shell.utils import check_ids

__version__ = "0.0.1"


def launch() -> None:
    print('\n\n')
    print('#' * 80)
    print('#\tPython controller for NewFocus Picomotor Controller')
    print('#' * 80)
    print('\n')
    parser = argparse.ArgumentParser(prog='Newport Shell',
                                     description='What the program does',
                                     epilog='Text at the bottom of help')
    parser.add_argument(
        '-o',
        '--open',
        dest='id',
        help='Open USB device. Parameters: `idVendor`:`idProduct`')
    args = parser.parse_args()
    console = ConsoleManager()
    if args.id:
        ids = check_ids(args.id)
        console.open(*ids)
    console.find()
