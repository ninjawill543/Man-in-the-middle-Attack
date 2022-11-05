import os
import subprocess



routerip = '192.168.1.254'

getVersion =  subprocess.Popen(("arp -a | grep " + (routerip)), shell=True, stdout=subprocess.PIPE).stdout
version =  getVersion.read()
routermac = (version.decode()).split()[3]


print(routermac)

