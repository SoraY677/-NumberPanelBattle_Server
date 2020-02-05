from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import json

PORT = 8000


class ServerHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        print("geted!")

    def do_POST(self):
        testjson = {'test':200}
        print("posted!")
        self.send_response(200)
        self.send_header("Content-type", "text/json")
        self.end_headers()
        responseBody = json.dumps(testjson)
        self.wfile.write(responseBody.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=ServerHandler):
    server_address=('', PORT)
    httpd=server_class(server_address, handler_class)
    print("サーバー起動@ " + str(PORT))
    httpd.serve_forever()

if __name__ == '__main__':
    run()
