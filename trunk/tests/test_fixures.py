# -*- coding: utf-8 -*-
"""
Testing the fixures
"""
# $Id: test_fixures.py 6796 2007-12-04 10:52:51Z glenfant $

import unittest
import sys
import os
import fixures

class FixuresTest(unittest.TestCase):
    """Testing the tests environment
    """
    def test_syspath(self):
        """Do we include the openxmllib package in sys.path
        """
        self.failUnless(fixures.parent_dir in sys.path,
                             "%s not in sys.path" % fixures.parent_dir)
        sp_copy = list(sys.path)
        sp_copy.remove(fixures.parent_dir)
        self.failIf(fixures.parent_dir in sp_copy,
                    "%s should appear only once in sys.path" % fixures.parent_dir)
        return


    def test_testdir(self):
        """Do we have test data
        """
        self.failUnless(os.path.isdir(fixures.TEST_FILES_IN),
                        "We have no test data")
        return


    def test_import(self):
        """Do we import our lovely package
        """

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
