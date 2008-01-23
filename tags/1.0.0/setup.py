#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
% python setup.py install
$Id: setup.py 6864 2007-12-06 14:09:09Z glenfant $
"""
from distutils.core import setup

setup(name='openxmllib',
      version='1.0.0',
      description='Open XML document library',
      long_description='Open XML document library',
      author='Gilles Lenfant',
      author_email='gilles.lenfant@gmail.com',
      url='http://code.google.com/p/openxmllib/',
      license="GPLv2",
      packages=['openxmllib'],
      scripts=['scripts/openxmlinfo.py']
      )

try:
    import lxml
except ImportError, e:
    print "openxmllib will not work without lxml. Please install it (see README)"
