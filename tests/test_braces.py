from __future__ import absolute_import, print_function
import unittest
import os
import subprocess

from _resources import brace_error

__author__ = 'Alex'


class BraceTester(unittest.TestCase):
    def setUp(self):
        self.core = os.path.join(os.path.dirname(os.path.dirname(__file__)), "core.py")
        self.brace_error = os.path.join(os.path.dirname(brace_error.__file__), "brace_error.py")
        self.expected_results = [

        ]

    def test(self):
        args = ["python", self.core, self.brace_error]
        print(args)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        std_out, std_err = proc.communicate()
        print(std_err)


        self.assertEqual(std_err, self.expected_results)

if __name__ == "__main__":
    unittest.main()
