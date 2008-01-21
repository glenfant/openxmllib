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
The Open XML document library
Open XML document is defined by the ECMA-376 standard
http://www.ecma-international.org/publications/standards/Ecma-376.htm
"""
# $Id: __init__.py 6864 2007-12-06 14:09:09Z glenfant $

version_info = (1, 0, 0)
version = '.'.join([str(x) for x in version_info])

import os

import wordprocessing
import spreadsheet
import presentation

_document_classes = (
    wordprocessing.WordprocessingDocument,
    spreadsheet.SpreadsheetDocument,
    presentation.PresentationDocument)

def openXmlDocument(file_or_path_or_body, mime_type=None):
    """Factory function
    Will guess what document type is best suited and return the appropriate
    document type.
    # FIXME: this is very poor at the moment
    @param file_or_path_or_body: file object or path to file or file body.
    @param mime_type: mime type if known
    @return : Document subclass object
    Warning, when passing a file body, the mime_type is required
    """

    # Mime type based document
    if mime_type is not None:
        for klass in _document_classes:
            if klass.canProcessMime(mime_type):
                return klass(file_or_path_or_body, mime_type=mime_type)
        raise ValueError("%s MIME type is unknown." % mime_type)

    # File extension based factory
    if hasattr(file_or_path_or_body, 'read'):
        # File like object
        filename = file_or_path_or_body.name
    else:
        filename = os.path.basename(file_or_path_or_body)
    for klass in _document_classes:
        if klass.canProcessFilename(filename):
            return klass(file_or_path_or_body)
    raise ValueError("'%s' document cannot be processed here." % filename)

