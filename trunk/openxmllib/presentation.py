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
The presentation module handles a PresentationML Open XML document (read *.pptx)
"""
# $Id: presentation.py 6800 2007-12-04 11:17:01Z glenfant $

import document
from utils import IndexableTextExtractor
import contenttypes as ct


class PresentationDocument(document.Document):
    """Handles specific features of a PresentationML document"""

    _extpattern_to_mime = {
        '*.pptx': ct.CT_PRESENTATION_PPTX_PUBLIC,
        '*.pptm': ct.CT_PRESENTATION_PPTM_PUBLIC,
        '*.potx': ct.CT_PRESENTATION_POTX_PUBLIC,
        '*.potm': ct.CT_PRESENTATION_POTM_PUBLIC,
        '*.ppsx': ct.CT_PRESENTATION_PPSX_PUBLIC,
        '*.ppsm': ct.CT_PRESENTATION_PPSM_PUBLIC,
        # FIXME: Not sure we can honour below types
#        '*.ppam': ct.CT_PRESENTATION_PPAM_PUBLIC
        }

    _text_extractors = (
        IndexableTextExtractor(ct.CT_PRESENTATION_SLIDE, 'presentation-main:t'),
        )
    pass
