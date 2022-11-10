from scapy.all import sniff, DNS, DNSQR, DNSRR


if (sniff(prn=lambda x: x.show(), filter="port 53",promisc=1))[0].haslayer(DNS) and [0].getlayer(DNS).qr==0:
    print ([0].getlayer(DNS).qd.qname)
    print ([0].getlayer(DNS).qd.qtype)
    print ([0].getlayer(DNS).qd.qclass)
    print ([0].getlayer(DNS).id)
    print ([0].getlayer(DNS).an)
    print ([0].getlayer(DNS).ns)
    print ([0].getlayer(DNS).ar)
    

