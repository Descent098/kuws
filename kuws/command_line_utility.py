"""The primary entrypoint for the kuws script.

This module's main function contains all the argument
parsing for the kuws script.

Functions
---------
main:
    Primary entrypoint for the kuws script.

Module Variabes
---------------
usage : str
    A variable that defines the argument parsing for the script in standard POSIX format.

"""

# Python Standard library
import argparse
import sys
import os

# External Dependencies
from docopt import docopt

# Internal Dependencies
from .utilities.youtube import download
from .utilities.redirects import trace
from .utilities.ssl import check_ssl_expiry
from .utilities.domains import register_key

usage = """Kieran's Useful Web Scripts; A set of python web utility scripts.

Usage:
    kuws --version
    kuws (-h | --help)
    kuws ssl <url> [-e]
    kuws redirects <url> [-t]
    kuws domains [-k=<whoiskey>]
    kuws domains <domain> [-e] [-k=<whoiskey>]

Options:
    -h --help               Show this help message and exit
    -v --version            Show program's version number and exit
    -e --expiry             If specified will check the expiry of ssl cert/domain
    -t --trace              If specified will show the full trace of the provided url
    -k --key=<whoiskey>     If specified will register the whois domain key SEE: https://jsonwhois.io/

"""

def main():
    """Primary entrypoint for the kuws script."""
    args = docopt(usage, version="kuws V0.0.6") # Grab arguments for parsing

    if args["ssl"]: # Begin parsing for ssl subcommand
        if args["--expiry"]: # If -e or --expiry is specified
            check_ssl_expiry(args["<url>"], print_result=True)
    
    if args["redirects"]: # Begin parsing for redirects subcommand
        if args["--trace"]: # If -t or --trace is specified
            trace(args["<url>"], print_result=True)

    if args["domain"]: # Begin parsing for ssl subcommand
        if args["--expiry"]: # If -e or --expiry is specified
            pass
        if args["--key"]:
            register_key(args["--key"])
