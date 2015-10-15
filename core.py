__author__ = 'Alex'
import sys
import os, types
from pprint import pprint
import rules
import logging
logging.basicConfig(level=logging.DEBUG)


def bak_file(path):
    name, ext = os.path.splitext(path)
    new_ext = ".bak"
    return name + new_ext


def tag(name):
    return "# Modified by %s\n" % name


def remove_header(lines, header):
    for line in lines:
        if line[0] == "#":
            if line != tag(header):
                yield line
        else:
            yield line


def parse_args():
    python_file = None
    is_first = True
    for arg in sys.argv:
        if is_first:
            is_first = False
            continue
        elif os.path.exists(arg):
            if os.path.splitext(arg)[1] == ".py":
                # Is a py
                python_file = arg

    return python_file, sys.argv[1:]


def parse_mod(mod, bip):
    lines = remove_header(bip, mod.__name__)
    yield tag(mod.__name__)
    for line in lines:
        if isinstance(mod, types.ModuleType):
            new = mod.main(line)
            yield new


def parse_file(binary_data):
    new_lines = binary_data
    mods = rules.__all__
    for mod in mods:
        new_lines = parse_mod(mod, new_lines)
        logging.debug("Modified with %s" % mod.__name__)
    return new_lines

if __name__ == "__main__":
    py_file, args = parse_args()

    if py_file:
        data = None
        with open(py_file, "rb") as fh:
            data = fh.readlines()

        if data:
            corrected = parse_file(data)
            with open(bak_file(py_file), "wb") as fh:
                fh.writelines(data)
            with open(py_file, "wb") as fh:
                fh.writelines(corrected)
    else:
        print "Warning: No python file passed. Nothing was changed. Arg list was %s" % args
