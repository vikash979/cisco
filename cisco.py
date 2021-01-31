import shutil
import getpass
username = getpass.getuser() ### Used to get the username 


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

host_user = input("Enter your telnet username: ")
HOST_IP = input("Enter your telnet HOST_IP: ")
remoteusername = host_user+"@"+HOST_IP
print(remoteusername)

FILE = "Fir.pdf"
subprocess.run(["scp", FILE, remoteusername+":path"])

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

import mysql.connector as mysql
conn = mysql.connect("localhost","root","","dbname")
cursor = conn.cursor()
cursor.execute("CREATE TABLE table1 (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")
query = "INSERT INTO table1 (name, user_name) VALUES ('Ajjet','sjeet979'),('mohan','mohan979')................."
cursor.execute(query)
db.commit()



##########################################Token Base Authentication####################################################

"""
in django setting file

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-Party Apps
    'rest_framework',
    'rest_framework.authtoken',  # <-- Here

    # Local Apps (Your project's apps)
    'myapi.apps',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # <-- And here
    ],
}

"""


"""
in view.py
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class MyApiView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)




#####################update the router details based on ip


import mysql.connector as mysql
conn = mysql.connect("localhost","root","","dbname")
cursor = conn.cursor()
cursor.execute("CREATE TABLE table1 (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, destination VARCHAR(255), gateway VARCHAR(255))")
query = "update table1 set (destination=0.0.0.0) where gateway=192.168.0.8"
cursor.execute(query)
db.commit()

########################list of router
sql_select_Query = "select * from table1 where ip >---"
cursor = conn.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()
cursor.close()

##########################################delete router

delet_router = "delete from table1 where ip =''"
cursor = conn.cursor()
cursor.execute(delet_router)
cursor.close()


#####################################################sample layout to make calls



re_path(r'^myapy_detail/$', views.MyApiView.as_view(), name="myapy_detail"),
