
Question1 = """

question 1
"""
print(Question1)
import telnetlib
import getpass
import sys
HOST_IP = input("Enter your telnet HOST_IP: ")
host_user = input("Enter your telnet username: ")
password = getpass.getpass()

import getpass
import telnetlib

HOST = "http://localhost:8000/"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("login: ")
tn.write(host_user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ls\n")
tn.write("exit\n")

print(tn.read_all())

print("\r")


import os
import zipfile

zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk("mydirectory"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()