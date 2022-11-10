from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP


a=sniff(count=5, prn=lambda x: x.show(), filter="port 53",promisc=1)
    #ipdest = 
    #udpdestport = 
    #dnsid = 

