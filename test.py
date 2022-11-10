from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP


a=sniff(count=10, prn=lambda x: x.show(), filter="port 53",promisc=1)
if a[0].haslayer(DNS) and a[0].getlayer(DNS).qr==1:
    print (a[0].getlayer(DNS).qd.qname)
    print (a[0].getlayer(DNS).qd.qtype)
    print (a[0].getlayer(DNS).qd.qclass)
    print (a[0].getlayer(DNS).id)
    print (a[0].getlayer(DNS).an)
    print (a[0].getlayer(DNS).ns)
    print (a[0].getlayer(DNS).ar)