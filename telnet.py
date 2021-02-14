#!/usr/bin/env python3
import telnetlib
import getpass
import sys

HOST="localhost"
#input("Enter your telnet HOST_IP: ")
host_user = "vikash"
#input("Enter your telnet username: ")
#password = "sudha"
password  = getpass.getpass()
#import getpass

#HOST = "http://localhost:8000/"
#user = input("Enter your remote account: ")
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST)
tn.read_until(b"login: ")
tn.write(host_user.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"touch file1\n")
tn.write(b"zip -r /tmp/test.zip file1\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))

print("\r")


#import os
#import zipfile

#zf = zipfile.ZipFile("myzipfile.zip", "w")
#for dirname, subdirs, files in os.walk("mydirectory"):
#    zf.write(dirname)
#    for filename in files:
#        zf.write(os.path.join(dirname, filename))
#zf.close()
