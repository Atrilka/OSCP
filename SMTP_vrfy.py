#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
  print "Usage: vrfy.py <ip> <username_list.txt>" 
  sys.exit(0)


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Create a Socket
connect=s.connect((sys.argv[1], 25))                  # Connect to the Server
banner=s.recv(1024)                                   # Receive the banner
print banner
with open(sys.argv[2]) as a:
	for line in a:
		s.send('VRFY ' + line + '\r')	      # VRFY a user
		result=s.recv(1024)
		print result
		if 'str' in line:
			break
s.close()		                              # Close the socket
                                          
#for user in $(cat users.txt);do echo VRFY $user |nc -nv -w 1 IP_address 25 2>/dev/null |grep ^"250";done
