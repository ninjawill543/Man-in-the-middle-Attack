from scapy.all import sniff, DNS, pkt, IP


a=sniff(filter="port 53",count=1,promisc=1)
if a[0].haslayer(DNS):
    print(pkt.getlayer(IP))
    print(pkt.getlayer(DNS))  