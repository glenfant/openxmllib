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

__all__ = ('TEST_FILES_IN', 'ALL_IN_FILES')
