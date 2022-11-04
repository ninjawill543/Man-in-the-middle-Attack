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
victim = input()
print("Chose the router:")
router = input()

print ("victim ip: ", ip[victim])
print ("victim mac: ", mac[victim])

print ("router ip: ", ip[router])
print ("router mac: ", mac[router])

    
    