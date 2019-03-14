from __future__ import print_function

import argparse
import sys
from typing import Optional
from typing import Sequence



def main(argv=None):  # type: (Optional[Sequence[str]]) -> int
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    tab_files = []

    for filename in args.filenames:
        with open(filename, 'r') as f:
            content = f.read()
            if '\t' in content:
                tab_files.append(filename)

    if tab_files:
        for tab_file in tab_files:
            print('Tab found: {}'.format(tab_file))
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
