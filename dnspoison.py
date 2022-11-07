from scapy.all import sniff, DNS, IP


a=sniff(count=1, prn=lambda x: x.show(), filter="port 53",promisc=1)
if a[0].haslayer(DNS) and a[0].gotlayer(DNS).qr==0:
   print (a[0].getlayer(DNS).id)
   print (a[0].getlayer(DNS).qname)
   print (a[0].getlayer(DNS).qtype)
   print (a[0].getlayer(DNS).qclass)