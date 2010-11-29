# -*- coding: utf-8 -*-
"""
The document modules handles an Open XML document
"""
# $Id$

import os
import tempfile
import zipfile
import shutil
import fnmatch
import urllib

import lxml

import contenttypes
from namespaces import ns_map
from utils import xmlFile
from utils import toUnicode


class Document(object):
    """**Base class for handling Open XML document (all types)**

    **Must** be subclassed for various types of documents (word processing, ...)

    :param file_: An opened file(like) object of the document that must be opened in 'rb' mode
    :param mime_type: the MIME type for the file, potentially found by :func:`openxmllib.openXmlDocument`
    """
    #: A mapping like ``{glob-expr: mime-type, ...}`` must be overriden by subclasses
    _extpattern_to_mime = {}

    #: A sequence of extractor objects for text extraction  must be overriden by subclasses
    _text_extractors = []

    def __init__(self, file_, mime_type=None):
        """**Creating a new document**
        """
        #: The MIME type of the document
        self.mime_type = mime_type

        # Some shortcuts
        op_sep = os.path.sep
        op_join = os.path.join
        op_isdir = os.path.isdir
        op_dirname = os.path.dirname

        # Preliminary settings depending on input
        #: The file mane of the document
        self.filename = getattr(file_, 'name', None)
        if self.filename is None and mime_type is None:
            raise ValueError("Cannot guess mime type from such object, you should use the mime_type constructor arg.")

        # Need to make a real file for urllib.urlopen objects
        if isinstance(file_, urllib.addinfourl):
            fh, self._cache_file = tempfile.mkstemp()
            fh = os.fdopen(fh, 'wb')
            fh.write(file_.read())
            fh.close()
            file_.close()
            file_ = open(self._cache_file, 'rb')

        # Inflating the zipped file
        self._cache_dir = tempfile.mkdtemp()
        openxmldoc = zipfile.ZipFile(file_, 'r', zipfile.ZIP_DEFLATED)
        for outpath in openxmldoc.namelist():

            # Makes Windows path when under Windows
            rel_outpath = op_sep.join(outpath.split('/'))
            abs_outpath = op_join(self._cache_dir, rel_outpath)
            abs_outdir = op_dirname(abs_outpath)
            if not op_isdir(abs_outdir):
                os.makedirs(abs_outdir)
            fh = file(abs_outpath, 'wb')
            fh.write(openxmldoc.read(outpath))
            fh.close()
        openxmldoc.close()
        file_.close()

        # Getting the content types declarations
        ct_file = op_join(self._cache_dir, '[Content_Types].xml')

        #: A :class:`openxmllib.contenttypes.ContentTypes` object for this document
        self.content_types = contenttypes.ContentTypes(xmlFile(ct_file, 'rb'))
        return


    @property
    def mimeType(self):
        """The official MIME type for this document, guessed from the extensions
        of the :py:attr:`openxmllib.document.Document.filename` attribute, as
        opposed to the :py:attr:`openxmllib.document.Document.mime_type`
        attribute.

        :return: ``application/xxx`` for this file
        """
        if self.mime_type:
            # Supposed validated by the factory
            return self.mime_type
        for pattern, mime_type in self._extpattern_to_mime.items():
            if fnmatch.fnmatch(self.filename, pattern):
                return mime_type


    @property
    def coreProperties(self):
        """Document core properties (author, ...) similar to DublinCore

        :return: mapping of standard metadata like ``{'title': 'blah', 'language': 'fr-FR', ...}``
        """
        return self._tagValuedProperties(contenttypes.CT_CORE_PROPS)


    @property
    def extendedProperties(self):
        """Additional document automatic properties provided by the office app

        :return: mapping of metadata like ``{'Pages': '14', ...}``
        """
        return self._tagValuedProperties(contenttypes.CT_EXT_PROPS)


    def _tagValuedProperties(self, content_type):
        """Document properties for property files having constructs like
        <ns:name>value</ns:name>

        :param content_type: ``contenttypes.CT_CORE_PROPS`` or ``contenttypes.CT_EXT_PROPS``
        :return: mapping like {'property name': 'property value', ...}
        """
        rval = {}
        if not content_type in self.content_types.listMetaContentTypes:
            # We fail silently
            return rval
        for tree in self.content_types.getTreesFor(self, content_type):
            for elt in tree.getroot().getchildren():
                tag = elt.tag.split('}')[-1] # Removing namespace if any
                rval[toUnicode(tag)] = toUnicode(elt.text)
        return rval


    @property
    def customProperties(self):
        """Document custom properties added by the document author.

        We canot convert the properties as indicated
        with the http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes
        namespace

        :return: mapping of metadata
        """
        rval = {}
        if len(self.content_types.getPathsForContentType(contenttypes.CT_CUSTOM_PROPS)) == 0:
            # We may have no custom properties at all.
            return rval
        XPath = lxml.etree.XPath # Class shortcut
        properties_xpath = XPath('custom-properties:property', namespaces=ns_map)
        propname_xpath = XPath('@name')
        propvalue_xpath = XPath('*/text()')
        for tree in self.content_types.getTreesFor(self, contenttypes.CT_CUSTOM_PROPS):
            for elt in properties_xpath(tree.getroot()):
                rval[toUnicode(propname_xpath(elt)[0])] = u" ".join(propvalue_xpath(elt))
        return rval


    @property
    def allProperties(self):
        """Helper that merges core, extended and custom properties

        :return: mapping of all properties
        """
        rval = {}
        rval.update(self.coreProperties)
        rval.update(self.extendedProperties)
        rval.update(self.customProperties)
        return rval


    def indexableText(self, include_properties=True):
        """Words found in the various texts of the document.

        :param include_properties: Adds words from properties
        :return: Space separated words of the document.
        """
        text = set()
        for extractor in self._text_extractors:
            for tree in self.content_types.getTreesFor(self, extractor.content_type):
                words = extractor.indexableText(tree)
                text |= words

        if include_properties:
            for prop_value in self.allProperties.values():
                if prop_value is not None:
                    text.add(prop_value)
        return u' '.join([word for word in text])


    def __del__(self):
        """Cleanup at Document object deletion
        """
        if hasattr(self, '_cache_dir'):
            shutil.rmtree(self._cache_dir, ignore_errors=True)
        if hasattr(self, '_cache_file'):
            os.remove(self._cache_file)
        return


    @classmethod
    def canProcessMime(cls, mime_type):
        """Check if we can process such mime type

        :param mime_type: Mime type as 'application/xxx'
        :return: True if we can process such mime
        """
        supported_mimes = cls._extpattern_to_mime.values()
        return mime_type in supported_mimes


    @classmethod
    def canProcessFilename(cls, filename):
        """Check if we can process such file based on name

        :param filename: File name as 'mydoc.docx'
        :return: True if we can process such file
        """
        supported_patterns = cls._extpattern_to_mime.keys()
        for pattern in supported_patterns:
            if fnmatch.fnmatch(filename, pattern):
                return True
        return False

