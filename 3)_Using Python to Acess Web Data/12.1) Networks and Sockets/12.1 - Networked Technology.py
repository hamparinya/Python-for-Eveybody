# Transport Control Protocol
# - Built on top of IP
# - Assume IP might list some data stores and retransmits data if it seems to be lost
# - Handles "flow control" using a transmit window
# - Provides a nice reliable pipe

# Sockets in Python

# Python has built-in support for TCP sockets
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
                    #   Host    ,  Port

# Application Protocol
# - Since TCP(and Python) gives us a reliable socket, what do we want to do with the socket? What problem do we want to solve?
# application photocol
# -- Mail
# -- World Wide Web

# HTTP - Hypertext Transfer Protocol
# - The dominant Application Layer Protocol on the Internet
# - Invented for the web- to Retrieve HTML, Imaages, Documents, etc
# - Extended to be data in addition to documents - RSS, Web Services, etc. Basic Concept - Make a Connection - Request a document - Retrieve the Document - Close th Connection.

# What is a Protocol?
# - A set of rules that all parties follow so we can predict each other's behavior
# - And not bump into each other
#       - On two-way roads in USA, drive on the right-hand side of the road
#       - On two-way raod in UK, drive on th left-hand side of the road.

# An HTTP Request in Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()