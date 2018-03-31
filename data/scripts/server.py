#!/usr/bin/env python

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import io
import json
import logging


class HS(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(
            self.path).encode('utf-8'))

        # post_data.json()
        j = json.loads(post_data.decode('utf-8'))
        print (j)
        for i in j['items']:
            
            if i['type'] == "call":
                print("Found call: %s", i['payload']['id'])

        return


def run(server_class=HTTPServer, handler_class=HS, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd port: %s\n', port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
