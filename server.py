#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import PotGenerator
import os
import logging
import logging.handlers
import sys
import time

from urlparse import urlparse, parse_qs

try:
	os.chdir('/home/pi/PotteryOnline/')
except:
	print 'executing from current direcory'

PORT = 8080

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


class MySimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		"""Serve a GET request."""
		#generate the pot before the stuff
		print "path"		
		print self.path
		if self.path == "/fig.jpg":
			print "new fig request"
			polyLimits = (-.1,.1,-.03,.03,-.0001,.0001)				
			g = PotGenerator.PolyPotGenerator(polyLimits)
			print g.numCurves,': ',[round(c,2) for poly in g for c in poly]
			g.plot(True)
			
		f = self.send_head()
		if f:
			try:
				

				#parse the query
				query_components = parse_qs(urlparse(self.path).query)				
				#res = query_components["res"] 
				print 'components %s'%query_components
				print urlparse(self.path).query
				self.copyfile(f, self.wfile)
			finally:
				f.close()

#logging from http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
LOG_FILENAME = "./logs/server.log"
LOG_LEVEL = logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
logHandler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=7)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

class MyLogger(object):
	def __init__(self, logger, level):
		"""Needs a logger and a Logger level."""
		self.logger = logger
		self.level = level
	def write(self, message):
		if message.rstrip() != "":
			self.logger.log(self.level, message.rstrip())

sys.stdout = MyLogger(logger, logging.INFO)
sys.stderr = MyLogger(logger, logging.ERROR)
#end logging
#usage: logger.info("bla bla") or print "..."

logger.info("starting server")

Handler = MySimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

logger.info("serving at port" + str(PORT))
print "serving at port", PORT
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.server_close()

#import daemon

#from spam import do_main_program

#with daemon.DaemonContext():
#	httpd.serve_forever()
