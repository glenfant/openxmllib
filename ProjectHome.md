# About #

**openxmllib** provides resources to handle OpenXML documents from Python.

OpenXML is the new office document format supported natively by MS Office 2007, and as import/export format by Apple iWork'08 and OpenOffice 2.2.

OpenXML is defined in the [ECMA-376](http://www.ecma-international.org/publications/standards/Ecma-376.htm) standard.

openxmllib runs on any platform that supports Python 2.4, 2.5 or 2.6 and the lxml Python library.



# New with openxmllib 1.0.7 #

zc.buildout friend

See more details [here](http://code.google.com/p/openxmllib/source/browse/tags/1.0.7/HISTORY).

# Features #

  * Extract indexable text from an OpenXML document.
  * Extract meta data from an OpenXML document (author, title, ...)

# Requirements #

openxmllib requires the lxml 1.3.x or later library. See how to install it in [lxml site](http://codespeak.net/lxml/).

# Installation (from tarball) #

Get the tarball with your browser, wget, curl or whatever, then:

```
  $ tar xfz openxmllib-x.y.y.tar.gz
  $ cd openxmllib-x.y.z
  $ sudo python setup.py install
```

# Installation from Cheeseshop #

Even easier that the tarball:

```
  $ [sudo] easy_install openxmllib
```

Note that this will install or upgrade a suited `lxml` library if you've not already go it.

# Usage #

```
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

```

# Console tool #

openxmllib comes with a shell command for testing of for use from a non Python app:

```
  $ openxmlinfo --help
```

# Planned features #

  * Transform OpenXML document to (poor) HTML for preview
  * Transform OpenXML document to plain unicode text preview