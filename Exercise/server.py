import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get('PORT', 80))

class SimpleHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, Docker!")

if __name__ == "__main__":
    with HTTPServer(('', PORT), SimpleHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()
