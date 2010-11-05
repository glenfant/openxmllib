# -*- coding: utf-8 -*-
"""
testing getting files from http protocol
"""

from fixures import *
from time import sleep
import unittest
import os
import openxmllib
import subprocess
import signal


THIS_DIR = os.path.dirname(__file__)
BASE_HTTP_SERVER_PATH = os.path.join(THIS_DIR, 'base_http_server.py')


class GettingFromUrl(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(GettingFromUrl, self).__init__(*args, **kwargs)
        self._server_process = subprocess.Popen(
            ['python', BASE_HTTP_SERVER_PATH],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        sleep(1)
        return

    def __del__(self):
        os.kill(self._server_process.pid, signal.SIGKILL)
        return

    def setUp(self):
        # here it is asummed you have started the base_http_server.py
        self.doc = openxmllib.openXmlDocument(url=DOCX_URL)
        return

    def test_indexableText(self):
        """Indexable text with properties"""
        itext = self.doc.indexableText()
        for word in (u'A', u'full', u'chàractèrs', u'non',
                     u'custom_value_2', u'title'):
            self.failUnless(word in itext, "%s was expected" % word)

    def test_indexableTextNoprop(self):
        """Indexable text without properties"""
        itext = self.doc.indexableText(include_properties=False)
        for word in (u'A', u'full', u'chàractèrs', u'non'):
            self.failUnless(word in itext, "%s was expected" % word)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GettingFromUrl))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
