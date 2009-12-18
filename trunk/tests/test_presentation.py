# -*- coding: utf-8 -*-
"""
Testing PresentationDocument
"""
# $Id$

import unittest
import os
from fixures import *

import openxmllib

class PresentationTest(unittest.TestCase):
    """Testing querying properties from a document"""

    def setUp(self):
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[2])
        self.doc = openxmllib.openXmlDocument(path=test_file_path)
        return


    def test_indexableText(self):
        """Indexable text with properties"""

        itext = self.doc.indexableText().split()
        some_words = (u'Chapter', u'presentation', u'proud', u'three', u'two',
             u'four', u'item', u'one', u'My', u'midword')
        some_words += (u'false', u'Microsoft Office PowerPoint')
        for word in some_words:
            self.failUnless(word in itext, "%s was expected in %s" % (word, itext))
        return


    def test_indexableTextNoprop(self):
        """Indexable text without properties"""

        itext = self.doc.indexableText(include_properties=False).split()
        some_words = (u'Chapter', u'presentation', u'proud', u'three', u'two',
             u'four', u'item', u'one', u'My')
        for word in some_words:
            self.failUnless(word in itext, "%s was expected in %s" % (word, itext))
        return
# /class WordProcessingTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PresentationTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
