from scapy.all import sniff, DNS, IP


a=sniff(filter="port 53",count=1,promisc=1)
if a[0].haslayer(DNS):
    print(a.getlayer(IP).src)
    print(a.getlayer(DNS).src)  