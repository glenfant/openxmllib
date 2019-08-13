# -*- coding: utf-8 -*-
# $Id$
"""
The Open XML document library
Open XML document is defined by the ECMA-376 standard
http://www.ecma-international.org/publications/standards/Ecma-376.htm
"""

import os
from io import StringIO

try:
    from urllib2 import urlopen  # py2
except ImportError:
    from urllib.request import urlopen  # py3
import mimetypes

from . import wordprocessing
from . import spreadsheet
from . import presentation

# TODO: is this used? version.txt is omitted on pip install
# version = None
# if version is None:
#     version = open(os.path.join(os.path.dirname(__file__), 'version.txt')).read().strip()

_document_classes = (
    wordprocessing.WordprocessingDocument,
    spreadsheet.SpreadsheetDocument,
    presentation.PresentationDocument)


def openXmlDocument(path=None, file_=None, data=None, url=None, mime_type=None):
    """**Factory function**

    Will guess what document type is best suited and return the appropriate
    document type.
    User must provide either ``path``, ``file_``, ``data`` or ``url`` parameter.

    :param path: file path in the local filesystem to a document.
    :param file_: a file (like) object to a document (must be opened in 'rb' mode')
    :param data: the binary data of a document
    :param url: the URL of a document
    :param mime_type: mime type if known. One of the known MIME types from :mod:`openxmllib.contenttypes`.

    Note that ``mime_type`` parameter **must** be provided if you provide the
    Open XML document through the ``data`` parameter. Otherwise, if you don't
    provide one, we'll try to guess which is the most appropriate using the file
    extension.

    :return: A subclass of :class:`openxmllib.document.Document`.
    """
    if path is not None:
        file_ = open(path, 'rb')
    elif file_ is not None:
        assert hasattr(file_, 'read')
    elif url is not None:
        file_ = urlopen(url)
        if mime_type is None:
            mime_type = file_.headers.gettype()
    elif data is not None:
        # file_ = StringIO(data) # needed anymore? data should be type bytes
        file_ = data
        assert mime_type is not None
    else:
        raise ValueError("Either path, file_, data, or url should be provided")

    # Mime type based document
    if mime_type is not None:
        for class_ in _document_classes:
            if class_.canProcessMime(mime_type):
                return class_(file_, mime_type=mime_type)
        raise ValueError("%s MIME type is unknown." % mime_type)

    else:
        assert hasattr(file_, 'name')

        for class_ in _document_classes:
            if class_.canProcessFilename(file_.name):
                return class_(file_, mime_type=mime_type)
        raise ValueError("Can't guess mime_type. You should set the mime_type param")


# Extending standard mimetypes
for class_ in _document_classes:
    for pattern, mime_type in class_._extpattern_to_mime.items():
        mimetypes.add_type(mime_type, pattern[1:], True)
