import BaseHTTPServer, SimpleHTTPServer
import ssl, sys
import os.path

if len(sys.argv) != 5:
  print 'Usage: python server.py certPath keyPath caPath port'
  sys.exit(1)


certPath = sys.argv[1]
keyPath = sys.argv[2]
caPath = sys.argv[3]
port = int(sys.argv[4])

if os.path.isfile(certPath):
  print 'Certificate found.'
else:
  print 'Certificate not found.'
  sys.exit(1)

if os.path.isfile(keyPath):
  print 'Private key found.'
else:
  print 'Private key not found.'
  sys.exit(1)

if os.path.isfile(caPath):
  print 'CA found.'
else:
  print 'CA not found.'
  sys.exit(1)

httpd = BaseHTTPServer.HTTPServer(('0.0.0.0', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, keyfile=keyPath, certfile=certPath, ca_certs=caPath, server_side=True)
httpd.serve_forever()
