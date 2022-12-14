""" Written by Benjamin Jack Cullen aka Holographic_Sol"""

import sys


def run_function_0(var_0):
    print('var_0:', var_0)


if len(sys.argv) == 2 and sys.argv[1] == '-h':
    print('')
    print('Title and description')
    print('    More description')
    print('')
    print('Command line arguments:')
    print('    -h  Displays this help message')
    print('')

run_function = ()
i = 0
for _ in sys.argv:
    if _ == '-f':
        var_0 = sys.argv[i+1]
        run_function = 0
        break

    i += 1

if run_function == 0:
    run_function_0()
