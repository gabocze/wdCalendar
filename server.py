import http.server
import socketserver

PORT = 8080

class H(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        self.do_GET()

Handler = H

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
