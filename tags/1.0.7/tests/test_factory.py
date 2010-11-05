# -*- coding: utf-8 -*-
"""
Testing construction on valid and crappy files through the factory
"""
# $Id: test_factory.py 6857 2007-12-05 17:57:56Z glenfant $

import unittest
import os
from fixures import *

import openxmllib
import openxmllib.contenttypes as ct

class FactoryTest(unittest.TestCase):
    """Testing construction of Document various ways"""


    def test_frompath(self):
        """Construction from a path"""

        for test_filename in ALL_IN_FILES:
            test_filepath = os.path.join(TEST_FILES_IN, test_filename)
            doc = openxmllib.openXmlDocument(test_filepath)
            self.failUnless(isinstance(doc, openxmllib.document.Document),
                            "%s should be processed" % test_filepath)
        return

    def test_fromfile(self):
        """Construction from a file file object"""

        for test_filename in ALL_IN_FILES:
            test_filepath = os.path.join(TEST_FILES_IN, test_filename)
            fh = file(test_filepath, 'rb')
            doc = openxmllib.openXmlDocument(test_filepath)
            fh.close()
            self.failUnless(isinstance(doc, openxmllib.document.Document),
                            "%s should be processed" % test_filepath)
        return

    def test_frommime(self):
        """Construction with a mimetype help"""

        # From file path
        mime_type = ct.CT_WORDPROC_DOCX_PUBLIC
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        doc = openxmllib.openXmlDocument(path=test_file_path, mime_type=mime_type)
        self.failUnless(isinstance(doc, openxmllib.wordprocessing.WordprocessingDocument),
                        "Failed to create with mime type %s" % mime_type)
        self.failUnlessEqual(doc.mimeType, mime_type)

        # From file object
        fh = file(test_file_path, 'rb')
        doc = openxmllib.openXmlDocument(file_=fh, mime_type=mime_type)
        fh.close()
        self.failUnless(isinstance(doc, openxmllib.wordprocessing.WordprocessingDocument),
                        "Failed to create with mime type %s" % mime_type)
        self.failUnlessEqual(doc.mimeType, mime_type)

        # From file content
        fh = file(test_file_path, 'rb')
        doc = openxmllib.openXmlDocument(data=fh.read(), mime_type=mime_type)
        fh.close()
        self.failUnless(isinstance(doc, openxmllib.wordprocessing.WordprocessingDocument),
                        "Failed to create with mime type %s" % mime_type)
        self.failUnlessEqual(doc.mimeType, mime_type)
        return
# /class FactoryTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(FactoryTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
