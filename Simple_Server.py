import http.server
import socketserver

try:
    port = 1234

    h = http.server.SimpleHTTPRequestHandler

    httpd =socketserver.TCPServer(("127.0.0.1",port),h)
    print(("[+]Server is Up....:"),port)
    httpd.serve_forever()
except Exception as error:
    print(("[-]Script Error"),error)
