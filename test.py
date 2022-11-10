from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP


a=sniff(count=10, prn=lambda x: x.show(), filter="port 53 qr 1",promisc=1)
