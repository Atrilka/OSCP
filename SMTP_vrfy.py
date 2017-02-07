#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
  print "Usage: vrfy.py <username>" 
  sys.exit(0)


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a Socket
connect=s.connect(('IP_address',25))                  # Connect to the Server
banner=s.recv(1024)                                   # Receive the banner
print banner
s.send('VRFY ' + sys.argv[1] + '\r\n')                # VRFY a user
result=s.recv(1024)
print result
s.close()                                             # Close the socket

#for user in $(cat users.txt);do echo VRFY $user |nc -nv -w 1 IP_address 25 2>/dev/null |grep ^"250";done
