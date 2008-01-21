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
The spreadsheet module handles a SpreadsheetML Open XML document (read *.xlsx)
"""
# $Id: spreadsheet.py 6800 2007-12-04 11:17:01Z glenfant $

import document
from utils import IndexableTextExtractor
import contenttypes as ct


class SpreadsheetDocument(document.Document):
    """Handles specific features of a SpreadsheetML document"""

    _extpattern_to_mime = {
        '*.xlsx': ct.CT_SPREADSHEET_XLSX_PUBLIC,
        '*.xlsm': ct.CT_SPREADSHEET_XLSM_PUBLIC,
        '*.xltx': ct.CT_SPREADSHEET_XLTX_PUBLIC,
        '*.xltm': ct.CT_SPREADSHEET_XLTM_PUBLIC,
        # FIXME: note sure we can honour below types...
#        '*.xlam': ct.CT_SPREADSHEET_XLAM_PUBLIC,
#        '*.xlsb': ct.CT_SPREADSHEET_XLSB_PUBLIC
        }

    _text_extractors = (
        IndexableTextExtractor(ct.CT_SPREADSHEET_SHAREDSTRINGS, 'spreadsheet-main:t'),
        )

    pass
