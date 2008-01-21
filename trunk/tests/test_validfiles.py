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
Testing construction on valid and crappy files
"""
# $Id: test_validfiles.py 6355 2007-09-20 17:16:21Z glenfant $

import unittest
import os
from fixures import *

import openxmllib

class DocumentConstructTest(unittest.TestCase):
    """Testing construction of Document various ways"""


    def setUp(self):
        self.test_file_path = os.path.join(TEST_FILES_IN, ALL_IN_FILES[0])
        return


    def test_file(self):
        """Construction from a file object"""

        fh = file(self.test_file_path, 'rb')
        doc = openxmllib.document.Document(fh)
        self._assertCreation(doc._cache_dir)
        return

    def test_path(self):
        """Construction from a file path"""

        doc = openxmllib.document.Document(self.test_file_path)
        self._assertCreation(doc._cache_dir)
        return

    def test_body(self):
        """Construction from a file content"""

        data = file(self.test_file_path, 'rb').read()
        doc = openxmllib.document.Document(data)
        self._assertCreation(doc._cache_dir)
        return

    def _assertCreation(self, path):
        self.failUnless(os.path.isfile(os.path.join(path, '[Content_Types].xml')),
                        "Expected to have data in path %s" % path)
        return

# /class DocumentConstructTest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DocumentConstructTest))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
