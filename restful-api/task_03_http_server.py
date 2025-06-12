#!/usr/bin/python3
"""
Task 3: Simple API using Python's http.server module.
Handles GET requests, serves JSON, and manages endpoints.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
    Custom request handler to manage different endpoints.
    """
    
    def do_GET(self):
        """
        Handles GET requests based on the path.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"name": "John", "age": 30, "city": "New York"})
            self.wfile.write(response.encode())
        
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"version": "1.0", "description": "A simple API built with http.server"})
            self.wfile.write(response.encode())
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server():
    """
    Starts the HTTP server on port 8000.
    """
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
