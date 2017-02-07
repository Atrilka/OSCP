#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 2:
  print "Usage: vrfy.py <username>" sys.exit(0)

# Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Connect to the Server connect=s.connect(('IP_address',25))

# Receive the banner
banner=s.recv(1024)
print banner

# VRFY a user
s.send('VRFY ' + sys.argv[1] + '\r\n') result=s.recv(1024)
print result

# Close the socket
s.close()

#for user in $(cat users.txt);do echo VRFY $user |nc -nv -w 1 IP_address 25 2>/dev/null |grep ^"250";done
