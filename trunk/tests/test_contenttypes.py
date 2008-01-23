# -*- coding: utf-8 -*-
"""
Testing ContentTypes object and services
"""
# $Id: test_contenttypes.py 6796 2007-12-04 10:52:51Z glenfant $

import unittest
import StringIO

from fixures import *

import openxmllib.namespaces as ns
import openxmllib.contenttypes as ct


CONTENTTYPES_XML = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="%(content-types)s">
  <Default Extension="jpeg" ContentType="image/jpeg" />
  <Default Extension="jpg" ContentType="image/jpeg" />
  <Default Extension="gif" ContentType="image/gif" />
  <Default Extension="png" ContentType="image/png" />
  <Default Extension="wmf" ContentType="image/x-emf" />
  <Default Extension="emf" ContentType="image/x-emf" />
  <Default Extension="tif" ContentType="image/tiff" />
  <Default Extension="tiff" ContentType="image/tiff" />
  <Default Extension="bin"
           ContentType="application/vnd.openxmlformats-officedocument.oleObject" />
  <Default Extension="rels"
           ContentType="application/vnd.openxmlformats-package.relationships+xml" />
  <Default Extension="xml" ContentType="application/xml" />
  <Override PartName="/word/document.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml" />
  <Override PartName="/word/numbering.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml" />
  <Override PartName="/docProps/core.xml"
            ContentType="application/vnd.openxmlformats-package.core-properties+xml" />
  <Override PartName="/docProps/app.xml"
            ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml" />
  <Override PartName="/docProps/custom.xml"
            ContentType="application/vnd.openxmlformats-officedocument.custom-properties+xml" />
  <Override PartName="/word/styles.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml" />
  <Override PartName="/word/fontTable.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml" />
  <Override PartName="/word/settings.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml" />
  <Override PartName="/word/footnotes.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml" />
  <Override PartName="/word/endnotes.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml" />
  <Override PartName="/word/comments.xml"
            ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml" />
</Types>
""" % ns.ns_map


class ContentTypesTest(unittest.TestCase):
    """Testing the ContentTypes object"""


    def setUp(self):
        self.content_types = ct.ContentTypes(StringIO.StringIO(CONTENTTYPES_XML))
        return

    def test_overrides(self):
        """Checking some overrides"""

        self.failUnlessEqual(self.content_types.getPathsForContentType(ct.CT_CORE_PROPS),
                             ['/docProps/core.xml'])
        self.failUnlessEqual(self.content_types.getPathsForContentType(ct.CT_EXT_PROPS),
                             ['/docProps/app.xml'])
        self.failUnlessEqual(self.content_types.getPathsForContentType(ct.CT_CUSTOM_PROPS),
                             ['/docProps/custom.xml'])
        return
# /class ContentTypesTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ContentTypesTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
