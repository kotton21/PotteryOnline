#!/usr/bin/env python

import BaseHTTPServer
import SocketServer
import PotGenerator
import os
import logging
import logging.handlers
import sys
import time
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs

#os.chdir('/home/pi/PotteryOnline/')

PORT = 8080


class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		print self.path
		print self.command

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
