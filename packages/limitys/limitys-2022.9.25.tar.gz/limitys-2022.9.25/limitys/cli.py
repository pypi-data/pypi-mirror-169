"""CLI interface for overlap (Finnish: limitys) assesses sentences from constrained and overlapping vocabularies."""
import argparse
import pathlib
import sys
from typing import List, Union

import limitys.limitys as api
from limitys import APP_ALIAS, APP_NAME


def parse_request(argv: List[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--language',
        '-l',
        dest='language',
        required=False,
        default='english',
        help='language in (english, french, german, spanish) of the documents. Optional\n(default: english)',
    )
    parser.add_argument(
        '--documents',
        '-d',
        dest='documents',
        default='',
        help='file providing the keyed documents. Optional\n(default: positional documents value)',
        required=False,
    )
    parser.add_argument(
        'documents_pos',
        nargs='?',
        default='',
        help='file with format in (json, yaml) providing the keyed documents. Optional\n(default: documents.yml)',
    )
    parser.add_argument(
        '--out-path',
        '-o',
        dest='out_path',
        default=sys.stdout,
        help='output file path for matrix (default: STDOUT)',
    )
    parser.add_argument(
        '--quiet',
        '-q',
        dest='quiet',
        default=False,
        action='store_true',
        help='work as quiet as possible - progress bar only if all well (default: False)',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='work logging more information along the way (default: False)',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.verbose and options.quiet:
        parser.error('you cannot be quiet and verbose at the same time')

    if not options.documents:
        if options.documents_pos:
            options.documents = options.documents_pos
        else:
            options.documents = 'documents.yml'

    documents = pathlib.Path(options.documents)
    if documents.exists():
        if documents.is_file():
            return options
        parser.error(f'requested documents file at ({documents}) is not a file')

    parser.error(f'requested documents file at ({documents}) does not exist')


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.similarity(options)
