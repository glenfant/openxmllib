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
Namespaces that may be used in various XML files
"""
# $Id: namespaces.py 6800 2007-12-04 11:17:01Z glenfant $

CONTENT_TYPES = 'http://schemas.openxmlformats.org/package/2006/content-types'

# Properties (common for all openxml types)
CORE_PROPERTIES = 'http://schemas.openxmlformats.org/package/2006/metadata/core-properties'
EXTENDED_PROPERTIES = 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'
CUSTOM_PROPERTIES = 'http://schemas.openxmlformats.org/officeDocument/2006/custom-properties'

# Wordprocessing
WP_MAIN = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'

# Spreadsheet
SS_MAIN = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'

# Presentation
PR_MAIN = 'http://schemas.openxmlformats.org/drawingml/2006/main'

# Namespaces mapping useful for XPath expression shortcuts
ns_map = {
    'content-types': CONTENT_TYPES,
    'core-properties': CORE_PROPERTIES,
    'extended-properties': EXTENDED_PROPERTIES,
    'custom-properties': CUSTOM_PROPERTIES,
    'wordprocessing-main': WP_MAIN,
    'spreadsheet-main': SS_MAIN,
    'presentation-main': PR_MAIN
    }
