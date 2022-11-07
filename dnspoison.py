from scapy.all import sniff, DNS, IP, src


a=sniff(prn=lambda x: x.show(), filter="port 53",count=1,promisc=1)
if a[0].haslayer(DNS):
    print (a[0].getlayer(IP).src)
    print (a[0].getlayer(DNS).src)