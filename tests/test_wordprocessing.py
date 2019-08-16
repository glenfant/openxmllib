# -*- coding: utf-8 -*-
"""
Testing WordProcessingDocument
"""
# $Id: test_wordprocessing.py 6355 2007-09-20 17:16:21Z glenfant $

import os
import unittest

import openxmllib
from fixures import *


class WordProcessingTest(unittest.TestCase):
    """Testing querying properties from a document"""

    def setUp(self):
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        self.doc = openxmllib.openXmlDocument(path=test_file_path)
        test_template_file_path = os.path.join(TEST_FILES_IN, ALL_IN_TEMPLATE_FILES[0])
        self.template = openxmllib.openXmlDocument(path=test_template_file_path)
        return

    def test_indexableText(self):
        """Indexable text with properties"""

        itext = self.doc.indexableText().split()
        some_words = ('A', 'full', 'chàractèrs', 'non', 'custom_value_2', 'title', 'metadata')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return

    def test_indexableTextNoprop(self):
        """Indexable text without properties"""

        itext = self.doc.indexableText(include_properties=False).split()
        some_words = ('A', 'full', 'chàractèrs', 'non')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return

    def test_templateFile(self):
        """Template file (dotx)"""
        itext = self.template.indexableText().split()
        some_words = ('A', 'full', 'chàractèrs', 'non', 'custom_value_2', 'title', 'metadata')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return


# /class WordProcessingTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(WordProcessingTest))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
