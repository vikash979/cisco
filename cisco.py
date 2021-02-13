import shutil
import getpass
username = getpass.getuser() ### Used to get the username 
print("----------------------------",username)


import os
import pwd

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]
usernames = get_username()
print(usernames)




path = "/home/"+username+"/Documents"
stat = shutil.disk_usage(path)# to get the disk usage
print(stat)


###########################2 #############(c) inode use##############

import os

path = os.getcwd()
with os.scandir(path) as shutle:
    for entry in shutle:
        print(entry.name,"---",entry.inode())


######################list of file ls################
from subprocess import call
import subprocess

out  =  subprocess.call(["ls", "-l"] , shell=True)
print("Files:::", out)


###############################copy files from remote server using scp, FTP, SFTP

host_user = input("Enter your host username: ")
HOST_IP = input("Enter your host HOST_IP: ")
remoteusername = host_user+"@"+HOST_IP
print(remoteusername)

FILE = "Fir.pdf"
subprocess.run(["scp", FILE, remoteusername+":path"])


#############################FTP 
import ftplib
passwd = input("Enter your host password: ")
session = ftplib.FTP(remoteusername,usernames,passwd)
file = open('abc.jpg','rb')  
session.storbinary('def.jpg', file) 
file.close()
session.quit()


############################SFTP

import pysftp

with pysftp.Connection('hostname', username='me', password='secret') as sftp:

    with sftp.cd('/allcode'):           # temporarily chdir to allcode
        sftp.put('/pycode/filename')    # upload file to allcode/pycode on remote
        sftp.get('remote_file')         # get a remote file

#Example -------------- subprocess.run(["scp", FILE, "vikas@192.168.0.8:/home/vikas/Desktop/eoffice/"])



#FTP
from ftplib import FTP
from pathlib import Path

file_path = Path('Fir.pdf')

#with FTP('server.address.com', 'USER', 'PWD') as ftp, open(file_path, 'rb') as file:
 #       ftp.storbinary(f'STOR {file_path.name}', file)



##########################################2 Auto restart apache server#####################################

subprocess.call(['sudo', 'service','apache2', 'restart'])

######################################################insert 10 more values##################

