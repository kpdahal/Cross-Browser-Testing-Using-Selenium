import http.server as SimpleHTTPServer
import socketserver

#start local server- simple http server
def start_local_server():
    try:
        port=8000
        RequestHandler= SimpleHTTPServer.SimpleHTTPRequestHandler
        server = socketserver.TCPServer(("", port), RequestHandler)   
        server.serve_forever()
        print('Running localhost on port:%s' % port)
    except Exception as e:
        print("An error occured during local server run.",format(e))  