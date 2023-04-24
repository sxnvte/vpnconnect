#/usr/bin/env python

import os

# config

# select what you want to use. doas or sudo
useDoas = False
useSudo = False

login = ""

"""enter in login varable path to your credentials (for example. /home/user/Desktop/ovpnlogin.txt) for openvpn file. the file should look like this:

login
password

"""

# end of config 


print("vpnconnect v1 by sxnvte")

cmd = input("Enter your .ovpn file > ")

if useDoas == True:
    os.system(f"doas openvpn --config {cmd} --auth-user-pass {login}")
    print("Done!")
elif useSudo == True:
    os.system(f"sudo openvpn --config {cmd} --auth-user-pass {login}")
    print("Done!")
else:
    print("error! maybe because useDoas and useSudo are both on false! maybe that some other reason")


