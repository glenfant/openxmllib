# -*- coding: utf-8 -*-
"""
Testing SpreadsheetDocument
"""
# $Id$

import os
import unittest

import openxmllib
from fixures import *


class SpreadsheetTest(unittest.TestCase):
    """Testing querying properties from a document"""

    def setUp(self):
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[1])
        self.doc = openxmllib.openXmlDocument(path=test_file_path)
        test_template_file_path = os.path.join(TEST_FILES_IN, ALL_IN_TEMPLATE_FILES[1])
        self.template = openxmllib.openXmlDocument(path=test_template_file_path)
        return

    def test_indexableText(self):
        """Indexable text with properties
        """
        itext = self.doc.indexableText().split()
        some_words = ('this', 'is', 'a', 'spreadsheet', 'another', 'sum',
                      'myinfo1', 'myinfo2', 'title', 'subject', 'comments')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return

    def test_indexableTextNoprop(self):
        """Indexable text without properties
        """
        itext = self.doc.indexableText(include_properties=False).split()
        some_words = ('this', 'is', 'a', 'spreadsheet', 'another', 'sum')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return

    def test_templateFile(self):
        """Template file (xltx)"""
        itext = self.template.indexableText().split()
        some_words = ('this', 'is', 'a', 'spreadsheet', 'another', 'sum',
                      'myinfo1', 'myinfo2', 'title', 'subject', 'comments')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return


# /class SpreadsheetTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SpreadsheetTest))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
