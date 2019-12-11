# -*- coding: utf-8 -*-
"""
Testing construction on valid and crappy files
"""
# $Id: test_validfiles.py 6355 2007-09-20 17:16:21Z glenfant $

import os
import unittest

import openxmllib
from fixures import *


class DocumentConstructTest(unittest.TestCase):
    """Testing construction of Document various ways"""

    def setUp(self):
        self.test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        return

    def test_file(self):
        """Construction from a file object"""

        fh = open(self.test_file_path, 'rb')
        doc = openxmllib.document.Document(fh)
        self._assertCreation(doc._cache_dir)
        return

    def test_path(self):
        """Construction from a file path"""

        fh = open(self.test_file_path, 'rb')
        doc = openxmllib.document.Document(file_=fh)
        self._assertCreation(doc._cache_dir)
        return

    def test_body(self):
        """Construction from a file content"""

        fh = open(self.test_file_path, 'rb')
        doc = openxmllib.document.Document(file_=fh)
        self._assertCreation(doc._cache_dir)
        return

    def _assertCreation(self, path):
        self.assertTrue(os.path.isfile(os.path.join(path, '[Content_Types].xml')),
                        "Expected to have data in path %s" % path)
        return


# /class DocumentConstructTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DocumentConstructTest))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
