# -*- coding: utf-8 -*-
"""HTTP minimalistic server for URL access"""
# $Id$

import os
import BaseHTTPServer

from fixures import HOST_NAME, PORT, TEST_FILES_IN, ALL_IN_FILES
from openxmllib import contenttypes as ct

class SimpleHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/word.docx':
            self.send_response(200)
            self.send_header('Content-Type', ct.CT_WORDPROC_DOCX_PUBLIC)
            #'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            self.end_headers()
            self.wfile.write(open(os.path.join(TEST_FILES_IN, ALL_IN_FILES[0]), 'rb').read())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Not Found!")


if __name__ == '__main__':
    httpd = BaseHTTPServer.HTTPServer((HOST_NAME, PORT), SimpleHandler)
    httpd.serve_forever()
