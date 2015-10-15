from __future__ import unicode_literals
import os
import sys
import types
import rules
import logging

__author__ = 'Alex'
logging.basicConfig(level=logging.DEBUG)


def bak_file(path):
    """
    bak_file will return a path to a file that has the same name but has it's extension changed to ".bak"
    :param path: (unicode) String path.
    :return: (unicode) String path with the extension changed to ".bak"
    """
    name, ext = os.path.splitext(path)
    new_ext = ".bak"
    return name + new_ext


def _tag(name):
    """
    _tag will return a string "Modified by NAME" where NAME is the passed string.
    :param name: (unicode) String. Ideally the name of the module that is modifying.
    :return: (unicode) String with the value "Modified by NAME" where NAME is the passed string.
    """
    # TODO: Test this encoding in Python 3 to make sure it works.
    return "# Modified by %s\n".encode() % name


def _remove_header(lines, header):
    """
    _remove_header will search for the header in the list of lines, if it finds it, it doesnt yield back the line.
    :param lines: (list) List of data from an opened python file.
    :param header: (unicode) String to look for when searching the lines.
    :return: (Generator) Generator that will be populated with each line that doesnt match the header.
    """
    for line in lines:
        if line[0] == "#":
            if line != _tag(header):
                yield line
        else:
            yield line


def _parse_mod(rule, file_data):
    """
    _parse_mod will yield each line after the rule has modified it.
    :param rule: (types.ModuleType) A module that will modify the python file's data.
    :param file_data: (list) List of strings where each string is a line in the python file.
    :return: (Generator) Generator that will be populated with each line after it has been modified.
    """
    lines = _remove_header(file_data, rule.__name__)
    yield _tag(rule.__name__)
    for line in lines:
        if isinstance(rule, types.ModuleType):
            new = rule.main(line)
            yield new


def parse_file(file_data, rwd=None):
    """
    parse_file will take the list of strings from the python file and mutate it to conform to the rules.
    If a rwd is passed, it should export a list of modules that have a "main" function. These modules are the rules that
     will be used to modify the file. If no rwd is passed, default context is assumed.
    :param file_data: (list) List of strings where each string is a line in the python file.
    :param rwd: (unicode) Rule working directory. String path to a package that will mimic the Pepperoni rules package.
    :return: (list) List of the modified lines.
    """
    new_lines = file_data
    mods = rules.__all__

    if rwd:
        sys.path.insert(0, rwd)
        rule_package = __import__(rwd, globals(), locals(), ["__all__"])
        reload(rule_package)
        mods = rule_package.__all__
    for mod in mods:
        new_lines = _parse_mod(mod, new_lines)
        logging.debug(_tag(mod.__name__))
    return new_lines
