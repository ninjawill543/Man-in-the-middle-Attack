from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP


a=sniff(count=5, prn=lambda x: x.show(), filter="port 53",promisc=1)
if a[0].haslayer(DNS) and a[0].getlayer(DNS).qr==0:
    print (a[0].getlayer(DNS).qd.qname)
    f = open("test.txt", "a")
    f.write(a[0].getlayer(DNS).qd.qname)
    f.close()
    #ipdest = 
    #udpdestport = 
    #dnsid = 

