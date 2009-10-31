# -*- coding: utf-8 -*-
"""
Testing the utils module resources
"""
# $Id: test_utils.py 6796 2007-12-04 10:52:51Z glenfant $

import unittest
import os
from fixures import *

import openxmllib

class UtilsTest(unittest.TestCase):
    """Testing resources from the utilsmodule"""


    def test_xmlfile(self):
        """Working around absence of BOM support in lxml"""

        from lxml import etree
        test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        doc = openxmllib.openXmlDocument(test_file_path)
        toc_path = os.path.join(doc._cache_dir, '[Content_Types].xml')
        fh = openxmllib.utils.xmlFile(toc_path, 'rb')
        xml = etree.parse(fh)
        self.failUnless(isinstance(xml.getroot(), etree._Element), "Expected an XML element")
        return

    def test_tounicode(self):
        """Unicodizing an object"""
        toUnicode = openxmllib.utils.toUnicode

        # Non text object
        self.failUnlessEqual(toUnicode(AttributeError), AttributeError)

        # ASCII stuff
        self.failUnlessEqual(toUnicode('foo'), u'foo')

        # Unicode stuff
        self.failUnlessEqual(toUnicode(u'foo'), u'foo')
        return

    def test_itextractor(self):
        """IndexableTextExtractor"""
        IndexableTextExtractor = openxmllib.utils.IndexableTextExtractor
        from StringIO import StringIO
        from openxmllib.contenttypes import CT_WORDPROC_DOCUMENT
        from lxml import etree

        ite = IndexableTextExtractor(CT_WORDPROC_DOCUMENT, 'wordprocessing-main:t')
        indexables = ite.indexableText(etree.parse(StringIO(WP_MAIN_XML)))
        some_words = (u'A', u'full', u'chàractèrs', u'non')
        for word in some_words:
            self.failUnless(word in indexables,
                            "%s expected from %s" % (word, indexables))
        return

# /class UtilsTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UtilsTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())

###
## Test data
###

# Wordprocessing main document
# application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml


WP_MAIN_XML = """<?xml version="1.0" encoding="utf-8"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"
            xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">
  <w:body>
    <w:p>
      <w:pPr>
        <w:pStyle w:val="Standard" />
        <w:widowControl w:val="on" />
        <w:suppressAutoHyphens w:val="true" />
        <w:ind w:left="0" w:right="0" w:hanging="0" />
        <w:rPr><w:lang w:val="fr-FR" />
        </w:rPr>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:lang w:val="fr-FR" />
        </w:rPr>
        <w:t xml:space="preserve"
             xmlns:pxs="urn:cleverage:xmlns:post-processings:extra-spaces">A simple example of a .docx document </w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:b w:val="on" />
          <w:lang w:val="fr-FR" />
        </w:rPr>
        <w:t xml:space="preserve"
             xmlns:pxs="urn:cleverage:xmlns:post-processings:extra-spaces">with</w:t>
      </w:r><w:r><w:rPr><w:lang w:val="fr-FR" />
        </w:rPr><w:t xml:space="preserve"
                     xmlns:pxs="urn:cleverage:xmlns:post-processings:extra-spaces"> a full set of metadata. And some non ASCII chàractèrs.</w:t>
      </w:r>
    </w:p>
    <w:p>
      <w:pPr>
        <w:pStyle w:val="Standard" />
        <w:widowControl w:val="on" />
        <w:suppressAutoHyphens w:val="true" />
        <w:ind w:left="0" w:right="0" w:hanging="0" />
        <w:rPr>
          <w:lang w:val="fr-FR" />
        </w:rPr>
      </w:pPr>
    </w:p>
    <w:sectPr>
      <w:footnotePr>
        <w:pos w:val="pageBottom" />
        <w:numFmt w:val="decimal" />
        <w:numStart w:val="1" />
        <w:numRestart w:val="continuous" />
      </w:footnotePr>
      <w:endnotePr>
        <w:pos w:val="docEnd" />
        <w:numFmt w:val="lowerRoman" />
        <w:numStart w:val="1" />
      </w:endnotePr>
      <w:pgSz w:orient="portrait" w:w="11905" w:h="16837" />
      <w:pgMar w:top="1134"
               w:left="1134"
               w:bottom="1134"
               w:right="1134"
               w:header="1134"
               w:footer="1134"
               w:gutter="0" />
      <w:cols w:num="0" w:space="0" />
    </w:sectPr>
  </w:body>
</w:document>
"""
