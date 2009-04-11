# -*- coding: utf-8 -*-
"""
Executes all tests here
"""
# $Id: runalltests.py 6355 2007-09-20 17:16:21Z glenfant $

import os
import unittest

TestRunner = unittest.TextTestRunner
suite = unittest.TestSuite()

this_dir = os.path.dirname(os.path.abspath(__file__))

testfiles = [n[:-3] for n in os.listdir(this_dir)
             if n.startswith('test') and n.endswith('.py')]

for testfile in testfiles:
    module = __import__(testfile)
    if hasattr(module, 'test_suite'):
        suite.addTest(module.test_suite())

if __name__ == '__main__':
    TestRunner().run(suite)
