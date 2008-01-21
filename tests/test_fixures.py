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
Testing the fixures
"""
# $Id: test_fixures.py 6796 2007-12-04 10:52:51Z glenfant $

import unittest
import sys
import os
import fixures

class FixuresTest(unittest.TestCase):
    """Testing the tests environment"""

    def test_syspath(self):
        """Do we include the openxmllib package in sys.path"""

        self.failUnlessEqual(fixures.parent_dir, sys.path[0],
                             "%s not in sys.path" % fixures.parent_dir)
        sp_copy = list(sys.path)
        sp_copy.remove(fixures.parent_dir)
        self.failIf(fixures.parent_dir in sp_copy,
                    "%s should appear only once in sys.path" % fixures.parent_dir)
        return


    def test_testdir(self):
        """Do we have test data"""

        self.failUnless(os.path.isdir(fixures.TEST_FILES_IN),
                        "We have no test data")
        return

    def test_import(self):
        """Do we import our lovely package"""

        import openxmllib
        dummy = openxmllib.openXmlDocument
        return
# /class FixuresTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FixuresTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
