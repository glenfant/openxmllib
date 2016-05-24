# -*- coding: utf-8 -*-
"""
Testing cover image extraction
"""
# $Id$

import unittest
import os
from fixures import *

import openxmllib

class CoverExtractionTest(unittest.TestCase):
    """Testing extracting cover image from a document"""

    def setUp(self):

        file_paths = [os.path.join(TEST_FILES_IN, fn) for fn in ALL_IN_FILES]
        self.docs = [openxmllib.openXmlDocument(path=pth) for pth in file_paths]

        cover_file_paths = [os.path.join(TEST_FILES_IN, fn) for fn in ALL_IN_COVER_FILES]
        self.coverdocs = [openxmllib.openXmlDocument(path=pth) for pth in cover_file_paths]

    def test_coverPresent(self):
        """A cover image exists within document"""

        for doc in self.coverdocs:
            suffix, fp = doc.documentCover()
            self.failUnless(suffix=="jpg")
            self.failUnless(fp.name.endswith("thumbnail.jpeg"))

    def test_coverNotPresent(self):
        """There is no cover image embedded in document"""

        for doc in self.docs:
            self.failUnless(doc.documentCover() == None)

# /class CoverExtractionTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(CoverExtractionTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
