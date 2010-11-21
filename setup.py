# -*- coding: utf-8 -*-
# $Id$
from setuptools import setup, find_packages
import os

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read().strip()

name = 'openxmllib'

long_description = "\n\n".join((
    read('README.txt'),
    read('doc', 'source', 'TODO.txt'),
    read('doc', 'source', 'HISTORY.txt')))

setup(
    name='openxmllib',
    version=read('openxmllib', 'version.txt'),
    description='Provides resources to handle OpenXML documents.',
    long_description=long_description,
    author='Gilles Lenfant',
    author_email='gilles.lenfant@gmail.com',
    url='http://code.google.com/p/openxmllib/',
    license="GPLv2",
    keywords='Python OpenXML lxml Office2007 ECMA376',
    classifiers=[
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Topic :: Office/Business :: Office Suites",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Indexing",
        "Programming Language :: Python"
    ],
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={
        '': ['tests']
        },
    install_requires=['lxml>=1.3.0'],
    zip_safe=False,
    entry_points={
        'console_scripts': ['openxmlinfo = openxmllib.shell:openxmlinfo']
    },
    )
