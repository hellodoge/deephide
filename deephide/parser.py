import argparse
from deephide.preferences import *

parser = argparse.ArgumentParser()

parser.add_argument('action', help='hide/reveal', choices=['hide', 'reveal'])

parser.add_argument('-b', '--box', help='container for/of hidden data', type=str,
                    nargs='+', required=True)

parser.add_argument('-i', '--input', help='data to hide', type=str, nargs='+')

parser.add_argument('-o', '--output', help='container for revealed data', type=str)

parser.add_argument('-c', '--compress', default=0, type=int,
                    choices=range(-1, 10), help='compression level (-1 to set default level)')

parser.add_argument('-p', '--password', help='encryption password')


verbosity = parser.add_mutually_exclusive_group()

verbosity.add_argument('-v', '--verbose', dest='verbosity',
                       default=DEFAULT_VERBOSITY, action='store_const',
                       const=INCREASED_VERBOSITY, help='increase output verbosity')

verbosity.add_argument('-q', '--quiet', dest='verbosity',
                       action='store_const', const=SILENT_VERBOSITY,
                       help='run program quietly')
