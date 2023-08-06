import sys
from conex.cli_parsers import ArgumentParser
from conex.cli_parsers import EditableCommandParser
from conex.cli_parsers import ConfigCommandParser
from conex.cli_parsers import UploadCommandParser
from .ConexAPI import ConexAPI


__version = "0.0.1"


def _setup_parser(conex_api: ConexAPI):
    parser = ArgumentParser(prog=__package__)
    parser.add_argument("-v", "--version", action="version", version=__version)

    subparsers = parser.add_subparsers(title="subcommand", dest="subcommand")
    subparsers.required = True

    ConfigCommandParser.setup_command(subparsers, conex_api)
    EditableCommandParser.setup_command(subparsers, conex_api)
    UploadCommandParser.setup_command(subparsers, conex_api)

    return parser


def main(args=None):
    conex_api = ConexAPI()
    parser = _setup_parser(conex_api)

    if not args:
        args = sys.argv[1:]

    parsed = parser.parse_args(args)
    parsed.command_func(parsed)


if __name__ == "__main__":
    main()
