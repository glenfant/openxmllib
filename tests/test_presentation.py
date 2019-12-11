# -*- coding: utf-8 -*-
"""
Testing PresentationDocument
"""
# $Id$

import os
import unittest

import openxmllib

from fixures import *


class PresentationTest(unittest.TestCase):
    """Testing querying properties from a document"""

    def setUp(self):
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[2])
        self.doc = openxmllib.openXmlDocument(path=test_file_path)
        test_template_file_path = os.path.join(TEST_FILES_IN, ALL_IN_TEMPLATE_FILES[2])
        self.template = openxmllib.openXmlDocument(path=test_template_file_path)
        return

    def test_indexableText(self):
        """Indexable text with properties"""

        itext = self.doc.indexableText().split()
        some_words = ('Chapter', 'presentation', 'proud', 'three', 'two', 'four', 'item', 'one', 'My')
        some_words += ('false',)
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return

    def test_indexableTextNoprop(self):
        """Indexable text without properties"""

        itext = self.doc.indexableText(include_properties=False).split()
        some_words = ('Chapter', 'presentation', 'proud', 'three', 'two',
                      'four', 'item', 'one', 'My')
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return

    def test_templateFile(self):
        """Template file (potx)"""
        itext = self.template.indexableText().split()
        some_words = ('Chapter', 'presentation', 'proud', 'three', 'two',
                      'four', 'item', 'one', 'My')
        some_words += ('false',)
        for word in some_words:
            self.assertTrue(word in itext, "%s was expected in %s" % (word, itext))
        return


# /class WordProcessingTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PresentationTest))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
