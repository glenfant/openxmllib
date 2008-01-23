# -*- coding: utf-8 -*-
"""
Testing the properties (metadata) of a document
"""
# $Id: test_properties.py 6355 2007-09-20 17:16:21Z glenfant $

import unittest
import os
from fixures import *

import openxmllib

class PropertiesTest(unittest.TestCase):
    """Testing querying properties from a document"""

    def setUp(self):
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        self.doc = openxmllib.openXmlDocument(test_file_path)
        return

    def test_coreprops(self):
        """Core properties"""

        props = self.doc.coreProperties

        # We check only some props
        expected = {
            'language': 'fr-FR',
            'title': 'The title of the document'
            }
        for k, v in expected.items():
            self.failUnlessEqual(props[k], v)
        return

    def test_extprops(self):
        """Extended properties"""

        props = self.doc.extendedProperties

        # We check only some props
        expected = {
            'Pages': '1',
            'Words': '18',
            'Paragraphs': '1'}
        for k, v in expected.items():
            self.failUnlessEqual(props[k], v)
        return

    def test_customprops(self):
        """Custom properties"""

        props = self.doc.customProperties
        expected = {
            'custom_title_1': 'custom_value_1',
            'custom_title_2': 'custom_value_2',
            'custom_title_3': 'custom_value_3',
            'custom_title_4': 'custom_value_4',
            }
        for k, v in expected.items():
            self.failUnlessEqual(props[k], v)
        return
# /class PropertiesTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PropertiesTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
