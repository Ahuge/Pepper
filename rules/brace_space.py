__author__ = 'Alex'
import re


def main(line):
    sub = re.sub(r"(\(\s+)", r"(", line)
    sub = re.sub(r"(\s+\))", r")", sub)
    return sub
