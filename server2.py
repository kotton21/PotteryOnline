#!/usr/bin/env python

import BaseHTTPServer
import SocketServer
import PotGenerator
import os
import logging
import logging.handlers
import sys
import time
import sqlite3
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs

#os.chdir('/home/pi/PotteryOnline/')

PORT = 8080
#SERVER_CONNECTION

#TODO setup logging
LOG_FILENAME = "./logs/server.log"
LOG_LEVEL = logging.INFO
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
logHandler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", $
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

logger.log(LOG_LEVEL, "test logging")
logger.log(LOG_LEVEL, "Starting server2")


#TODO init sqlite server
#build class representation? or keep it flexible..?
#code to setup server if it doesnt exist?

sqlite_conn = sqlite3.connect('server.db')
sqlite_curs = sqlite_conn.cursor()
c.execute('''CREATE TABLE pots (id, filename, date)
CREATE TABLE potItems (id, order) 
CREATE TABLE potResponce (id, responce, date, address)

''') 


#check if server exists, notify and create if not.
#create table...
#create bla.
#done



class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		print self.client_address
		print self.path
		print self.command
		#input stream self.rfile
		#output stream self.wfile
		#self.error_message_format: dictionary; "code" and "message" and "explain"????
		
		#TODO send images
		#if self.path in (get all recent images from sqllite)
			#store response in sqllite
			#get new image from PotGenerator
			#save new images params and filename in sqllite
			#send response
		#else:
			#send response
	
	#when get image (id)
	#browser sends ImageTimestamp/Response on last image, then requests 
	#a new image (timestamped).
	#server sends image back to client. 

def run(server_class=BaseHTTPServer.HTTPServer,
        handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
