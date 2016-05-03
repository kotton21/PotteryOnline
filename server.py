import SimpleHTTPServer
import SocketServer
import PotGenerator



PORT = 8080

# Handler = SimpleHTTPServer.SimpleHTTPRequestHandler


class MySimpleHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		"""Serve a GET request."""
		f = self.send_head()
		if f:
			try:
				self.copyfile(f, self.wfile)
				polyLimits = (-.1,.1,-.03,.03,-.0001,.0001)				
				g = PotGenerator.PolyPotGenerator(polyLimits)
				print g.numCurves,': ',[round(c,2) for poly in g for c in poly]
				g.plot(True)
			finally:
				f.close()

Handler = MySimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()


#import daemon

#from spam import do_main_program

#with daemon.DaemonContext():
#	httpd.serve_forever()
