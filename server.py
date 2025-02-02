import http.server
import socketserver

PORT = 5090

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":  # Serve index.html for root requests
            self.path = "index.html"
        return super().do_GET()

# Start the server
with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
