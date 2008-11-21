# -*- coding: utf-8 -*-
"""
Testing WordProcessingDocument
"""
# $Id: test_wordprocessing.py 6355 2007-09-20 17:16:21Z glenfant $

import unittest
import os
from fixures import *

import openxmllib

class WordProcessingTest(unittest.TestCase):
    """Testing querying properties from a document"""

    def setUp(self):
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        self.doc = openxmllib.openXmlDocument(test_file_path)
        return


    def test_indexableText(self):
        """Indexable text with properties"""

        itext = self.doc.indexableText()
        some_words = (u'A', u'full', u'chàractèrs', u'non', u'custom_value_2', u'title')
        for word in some_words:
            self.failUnless(word in itext, "%s was expected" % word)
        return


    def test_indexableTextNoprop(self):
        """Indexable text without properties"""

        itext = self.doc.indexableText(include_properties=False)
        some_words = (u'A', u'full', u'chàractèrs', u'non')
        for word in some_words:
            self.failUnless(word in itext, "%s was expected" % word)
        return
# /class WordProcessingTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(WordProcessingTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
