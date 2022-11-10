from scapy.all import sniff, DNS, DNSQR, DNSRR, srp, IP


a=sniff(count=1, prn=lambda x: x.show(), filter="port 53",promisc=1)
if a[0].haslayer(DNS) and a[0].getlayer(DNS).qr==0 and a[0].getlayer(DNS).qd.qname==str("'reverseproxy.ynov.com.'"):
    print("yes")
    #ipdest = 
    #udpdestport = 
    #dnsid = 

