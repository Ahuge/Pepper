__author__ = 'Alex'
import re


def main(line):
    sub = re.sub(r"(\t)", r"    ", line)
    return sub
