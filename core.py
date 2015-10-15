from __future__ import unicode_literals
import sys
import logging

import click

import utils

__author__ = 'Alex'
logging.basicConfig(level=logging.DEBUG)


@click.command()
@click.argument('source')
@click.option('--d', default=None, type=click.STRING, help="Destination python file.")
@click.option('--backup', default=True, type=click.BOOL, help="Will backup the python file if --d was not set.")
@click.option('--write', default=True, type=click.BOOL, help="Writes the file out.")
@click.option('--rules', default=None, type=click.STRING, help="Optionally load the rules from this directory.")
def pepperoni(source, d, backup, write, rules):
    """
    Pepperoni will read the python file SOURCE and modify it to match PEP008 standards
    """

    if source:
        with open(source, "rb") as fh:
            data = fh.readlines()

        if data:
            corrected = utils.parse_file(data, rwd=rules)
            if d:
                dest = d
            else:
                if backup:
                    dest = utils.bak_file(source)
                else:
                    dest = source

            if write:

                with open(source, "wb") as fh:
                    fh.writelines(data)
                with open(dest, "wb") as fh:
                    fh.writelines(corrected)
            else:
                sys.stderr(corrected)
    else:
        print "Warning: No python file passed. Nothing was changed."

if __name__ == "__main__":
    pepperoni(None, None, None, None)
