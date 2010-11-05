# -*- coding: utf-8 -*-
"""
Environment fixures (stubs, data, ...) for unit testing
"""
# $Id: fixures.py 6796 2007-12-04 10:52:51Z glenfant $

import os
import sys

# Fixing the sys.path such "openxmllib" is on top
this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(this_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Unit tests notification
if not os.getenv('PYTHON_UNIT_TEST', False):
    os.putenv('PYTHON_UNIT_TEST', 'OK')

# Directories with test files
TEST_FILES_IN = os.path.join(this_dir, 'in')
ALL_IN_FILES = ('wordprocessing1.docx', 'spreadsheet1.xlsx', 'presentation1.pptx')
HOST_NAME = '127.0.0.1'
PORT = 8088
DOCX_URL = 'http://%s:%s/word.docx' % (HOST_NAME, PORT)

__all__ = ('TEST_FILES_IN', 'ALL_IN_FILES', 'DOCX_URL', 'HOST_NAME', 'PORT')
