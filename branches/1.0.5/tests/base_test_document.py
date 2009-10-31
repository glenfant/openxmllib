# -*- coding: utf-8 -*-
"""
Testing base_test_document
"""
# $Id$

import unittest
import os
from fixures import *

import openxmllib

class BaseTestDocument(unittest.TestCase):
    """Base testing querying properties from a document"""

    def setUp(self):
        self.document = openxmllib.openXmlDocument(self.test_file_path)


    def test_indexableText(self):
        """Base indexable text with properties"""

        indexable_text = self.document.indexableText()
        for indexable_word in self.indexable_words_with_properties:
            self.failUnless(indexable_word in indexable_text, "%s was expected" % indexable_word)


    def test_indexableTextNoprop(self):
        """Base indexable text without properties"""

        indexable_text = self.document.indexableText(include_properties=False)
        for indexable_word in self.indexable_words_without_properties:
            self.failUnless(indexable_word in indexable_text, "%s was expected" % indexable_word)

