# -*- coding: utf-8 -*-
## Copyright (C) 2007 Ingeniweb

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; see the file COPYING. If not, write to the
## Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

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
        self.doc = openxmllib.openXmlDocument(test_file_path)
        return


    def test_indexableText(self):
        """Indexable text with properties"""

        itext = self.doc.indexableText()
        some_words = (u'Chapter', u'presentation', u'proud', u'three', u'two',
             u'four', u'item', u'one', u'My')
        some_words += (u'false', u'Microsoft Office PowerPoint')
        for word in some_words:
            self.failUnless(word in itext, "%s was expected" % word)
        return


    def test_indexableTextNoprop(self):
        """Indexable text without properties"""

        itext = self.doc.indexableText(include_properties=False)
        some_words = (u'Chapter', u'presentation', u'proud', u'three', u'two',
             u'four', u'item', u'one', u'My')
        for word in some_words:
            self.failUnless(word in itext, "%s was expected" % word)
        return
# /class WordProcessingTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PresentationTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
