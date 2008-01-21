# -*- coding: utf-8 -*-
## Copyright (C) 2007 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

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
