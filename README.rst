==========
openxmllib
==========

openxmllib is a set of tools that deals with the new ECMA 376 office file
formats known as OpenXML.

http://www.ecma-international.org/publications/standards/Ecma-376.htm

OpenXML format is used by Microsoft Office 2007 and later. Apple iWork
and OpenOffice have filters to use this format too, starting from iWork'08
and OO version 2.2.

Features
========

Tested features
---------------

* Extract words from a document for indexing purpose.
* Get metadata from a document
* Add OpenXml mimetypes to standard ``mimetypes`` module.
* Extract cover thumbnail image, if the document contains it

Planned features
----------------

* Transform a document to HTML

Public API
==========

These examples say all::

  >>> import openxmllib
  >>> doc = openxmllib.openXmlDocument(path='office.docx')
  >>> # Raises a ValueError on not supported office files.
  >>> doc.mimeType
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
  >>> doc.coreProperties # Keys may depend on application
  {'title': u'blah...', u'creator': u'John Doe', ...}
  >>> doc.extendedProperties # Keys may depend on application
  {'Words': u'312', 'Application': u'Your favorite word processor', ...}
  >>> doc.customProperties # May return an empty mapping
  {'My property': u'My value', ...}
  >>> doc.allProperties # Merges core+extended+custom properties (see above)
  {...}
  >>> doc.indexableText(include_properties=False)
  u'all the words of that document body'
  >>> doc.indexableText(include_properties=True)
  u'all the words of that document body and all properties values'
  >>> doc.documentCover()
  ('jpg', <open file '/var/folders/.../docProps/thumbnail.jpeg', mode 'rb' at 0x1af300>)

Standard ``mimetypes`` package extensions ::

  >>> import mimetypes
  >>> mimetypes.guess_type('somedoc.docx')
  ('application/vnd.openxmlformats-officedocument.wordprocessingml.document', None)
  >>> mimetypes.guess_type('somecalc.xlsx')
  ('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', None)
  >>> mimetypes.guess_type('someslides.pptx')
  ('application/vnd.openxmlformats-officedocument.presentationml.presentation', None)

Document factory signatures::

  >>> # We have the path for the office file
  >>> doc = openxmllib.openXmlDocument(path='office.docx')
  >>> # We have a file object for the office file
  >>> fh = open('office.docx', 'rb')
  >>> doc = openxmllib.openXmlDocument(file_='office.docx')
  >>> # We have the URL for the office file
  >>> doc = openxmllib.openXmlDocument(url='http://domain.tld/office.docx')
  >>> # Xe have the raw data of the office file
  >>> import mimetypes
  >>> docx_mimetype = mimetypes.guess_type('office.docx')
  >>> body = open('office.docx', 'rb').read()
  >>> doc = open(data=body, mime_type=docx_mimetype)

Note that if you're not running a Python application, you may get the indexable
text from a document with the `openxmlinfo.py` console utility. Just type::

  $ openxmlinfo --help

Copying and License
===================

Copyright (c) 2008 Gilles Lenfant

This software is subject to the provisions of the GNU General Public
License, Version 2.0 (GPL).  A copy of the GPL should accompany this
distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY,
AGAINST INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE

More details in the ``COPYING`` file included in this package.

Status
======

Starting from version 1.1, this package is tested mostly using Python 2.7.x on
Linux. If dependencies can be met, it will most likely work on older versions
and other environments as well.

If you don't require the cover image extraction feature and want a production-
quality version tested on Mac OSX, Linux and Windows with Python 2.4, Python 2.5,
lxml 1.3.6 and lxml 2.2, it might be worth your while to try 1.0.7. It should
work on other platforms as well, with Python 2.6, perhaps with other versions of
lxml.


Installation
============

Using the usual setuptools command::

  $ [sudo] easy_install openxmllib

Note that this will install the excellent `lxml` egg too if not already done.

From now you can "import openxmllib" in your Python apps and use the
"openxmlinfo" command line utility.

Gotchas
=======

Be aware that most text data coming from the various openxmllib
services might be us-ascii or Unicode. This is a side effect of lxml
(bug or feature ?). It's up to your application to convert these texts
to the appropriate charset.

We do not actually handle exceptions due to malformed XML or various
unexpected structures. You should handle the various (potential)
problems in a try (...) except (...) block in your application.

Developing and testing
======================

You should grab openxmllib from its `repository at https://github.com/glenfant/openxmllib`_.

Then::

  $ cd /where/you/installed/openxmllib
  $ python setup.py develop

Note that testing does not require the installation::

  $ cd tests
  $ python runalltests.py

Support
=======

Use the issue tracker provided from the `project site
<https://github.com/glenfant/openxmllib/issues>`_.

Credits
=======

* Gilles Lenfant [gilles.lenfant] <gilles dot lenfant at gmail dot com>
* Kevin Deldycke [kevin.deldycke] <kevin at deldycke dot com>
* Hugo Lopes Tavares [hltbra] <hltbra at gmail dot com>
* Petri Savolainen [petri] <petri dot savolainen at koodaamo dot fi>
