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
The wordprocessing module handles a WordprocessingML Open XML document (read *.docx)
"""
# $Id: wordprocessing.py 6800 2007-12-04 11:17:01Z glenfant $

import document
from utils import IndexableTextExtractor
import contenttypes as ct


class WordprocessingDocument(document.Document):
    """Handles specific features of a WordprocessingML document"""

    _extpattern_to_mime = {
        '*.docx': ct.CT_WORDPROC_DOCX_PUBLIC,
        '*.docm': ct.CT_WORDPROC_DOCM_PUBLIC,
        '*.dotx': ct.CT_WORDPROC_DOTX_PUBLIC,
        '*.dotm': ct.CT_WORDPROC_DOTM_PUBLIC
        }

    _text_extractors = (
        IndexableTextExtractor(ct.CT_WORDPROC_DOCUMENT, 'wordprocessing-main:t'),
        )

    pass
