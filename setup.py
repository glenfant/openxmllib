# -*- coding: utf-8 -*-
"""
$Id: setup.py 6864 2007-12-06 14:09:09Z glenfant $
"""

from setuptools import setup, find_packages
import os


def read(*rnames):
  return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


name             = 'openxmllib'
version          = '1.0.1'
long_description = "%s\n%s\n%s" % (read('README'), read('TODO'), read('HISTORY'))


setup( name                 = name
     , version              = version
     , description          = 'Provides resources to handle OpenXML documents from Python.'
     , long_description     = long_description
     , author               = 'Gilles Lenfant'
     , author_email         = 'gilles.lenfant@gmail.com'
     , url                  = 'http://code.google.com/p/openxmllib/'
     , license              = "GPLv2"
     , keywords             = 'Python OpenXML lxml Office2007 ECMA376'
     , classifiers          = [ "License :: OSI Approved :: GNU General Public License (GPL)"
                              , "Topic :: Office/Business :: Office Suites"
                              , "Topic :: Software Development :: Libraries :: Python Modules"
                              , "Topic :: Utilities"
                              , "Programming Language :: Python"
                              ]
     , packages             = find_packages(name, exclude='tests')
     , package_dir          = {'': name}
     , include_package_data = True
     , install_requires     = ['lxml>=1.3.0,<2.0.0dev', ]
     , zip_safe             = False
     , scripts              = ['scripts/openxmlinfo.py', ]
     )

