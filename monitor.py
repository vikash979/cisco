import subprocess

out  =  subprocess.call(["netstat", "-s"] , shell=True)
print("Files:::", out)

##################aaaaaaaaaaaaaaaaaaaa@@@@@@@@

net_obs  =  subprocess.call(["traceroute", "4.2.2.2"])
print("Files:::", net_obs)



######################################bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

net_obs  =  subprocess.call(["htop" ],shell =True)
print("Files:::", net_obs)



import time

while True:
    range(10000)       # some payload code
    print("Me again")  # some console logging
    time.sleep(0.2)    # sane sleep time of 0.1 seconds

