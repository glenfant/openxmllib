# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import openxmllib

def read(*rnames):
  return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


name = 'openxmllib'
version = openxmllib.version
long_description = "%s\n%s\n%s" % (read('README'), read('TODO'), read('HISTORY'))

setup(name=name,
      version=version,
      description='Provides resources to handle OpenXML documents from Python.',
      long_description=long_description,
      author='Gilles Lenfant',
      author_email='gilles.lenfant@gmail.com',
      url='http://code.google.com/p/openxmllib/',
      license="GPLv2",
      keywords='Python OpenXML lxml Office2007 ECMA376',
      classifiers=["License :: OSI Approved :: GNU General Public License (GPL)",
                   "Topic :: Office/Business :: Office Suites",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                   "Topic :: Text Processing :: Indexing",
                   "Programming Language :: Python"
                   ],
      packages=find_packages(),
      include_package_data=True,
      install_requires=['lxml>=1.3.0'],
      zip_safe=False,
      scripts=['scripts/openxmlinfo.py']
     )
