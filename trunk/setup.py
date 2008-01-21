#! /usr/bin/env python
# -*- coding: utf-8 -*-
## Copyright (C) 2008 Gilles Lenfant

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
