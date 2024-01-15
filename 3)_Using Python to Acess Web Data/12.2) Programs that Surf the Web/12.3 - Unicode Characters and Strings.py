# Unicode charaters and Strings
# ASCII = American Standard Code for Information Interchange

# Representing Sample Strings
print(ord('H'))     # ord() is function tell us the numeric value of a simple ASCII character
print(ord('e'))     #-> 101
print(ord('\n'))    #-> 10

# Multi-Byte Characters
# To represent the wide range of characters computers must handle we represent characters with more one byte
#       UTF-16 -Fixed length - Two bytes
#       UTF-32 -Fixed length - Four bytes
#       UTF-8  -1-4 bytes
#           -Upwards compatible with ASCII
#           -Automatic detection between ASCII and UTF-8
#           -UTF-8 is recommend practice for encoding data to be exchange between systems

#Python 3 and Unicode
x = b'abc'              
print(type(x))      #In python 2  
                    # regular string vs byte strings  are the same
x = 'แฮม'           # regular string vs unicode strings are  difference
print(type(x))      #In python 3
                    # regular string vs byte strings  are differnce
x = u'แฮม'          # regular string vs unicode strings are  the same    
print(type(x))      # all stings are unicode. UTF-8


import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)
# Python Strings to Bytes
while True:
    data = mysock.recv(512) # data is Bytes
    if (len(data) < 1):
        break
    mystring = data.decode()    # mystring is Unicode, .decode() is a UTF-8 on ASCII
    print(mystring)
