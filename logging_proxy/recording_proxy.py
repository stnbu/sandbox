#!/usr/bin/env python3

import socketserver
import http.server
#import SimpleHTTPServer
import urllib

PORT = 3175

class RecordingProxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        breakpoint()
        url=self.path[1:]
        self.send_response(200)
        self.end_headers()
        self.copyfile(urllib.urlopen(url), self.wfile)


if __name__ == "__main__":
    httpd = socketserver.ForkingTCPServer(('', PORT), RecordingProxy)
    print ("Now serving at %s" % str(PORT))
    httpd.serve_forever()
