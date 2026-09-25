import http.server
import socketserver

PORT = 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()
