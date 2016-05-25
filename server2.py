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
DB_NAME = 'server.db'
LOG_FILENAME = "./logs/server.log"
LOG_LEVEL = logging.INFO



#TODO init sqlite server
#build class representation? or keep it flexible..?
#code to setup server if it doesnt exist?
#class ServerDB:
#	def __init__(self, name):
#		self.server_name = name

#check if server exists, notify and create if not.
#create table...
#create bla.
#done

class MyLogger(object):
        def __init__(self, logger, level):
                '''Needs a logger and a Logger level.'''
                self.logger = logger
                self.level = level
        def write(self, message):
                if message.rstrip() != "":
                        self.logger.log(self.level, message.rstrip())

class MyHTTPRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		print self.client_address
		print self.path
		print self.command
		#input stream self.rfile
		#output stream self.wfile
		#self.error_message_format: dictionary; "code" and "message" and "explain"??
		
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
	'''Main method for server2.py'''

	logger = logging.getLogger(__name__)
	logger.setLevel(LOG_LEVEL)
	logHandler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=7)
	formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
	logHandler.setFormatter(formatter)
	logger.addHandler(logHandler)
	
	logger.log(LOG_LEVEL, "test logging")
	logger.log(LOG_LEVEL, "Starting server2")

	sys.stdout = MyLogger(logger, logging.INFO)
	sys.stderr = MyLogger(logger, logging.ERROR)

	if DB_NAME not in os.listdir(os.getcwd()):
		logger.log(LOG_LEVEL, "initializing "+DB_NAME)
		sqlite_conn = sqlite3.connect(DB_NAME)
		curs = sqlite_conn.cursor()
		ret = curs.execute('''CREATE TABLE pots (id real, filename text, date text); CREATE TABLE potItems (id real, order real, c1 real, c2 real, c3 real, xoff real);
CREATE TABLE potResponce (id real, responce text, date text, address text);''' 
		) 	

	server_address = ('', 8000)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()

run()

