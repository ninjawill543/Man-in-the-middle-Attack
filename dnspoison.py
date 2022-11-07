from scapy.all import sniff, DNS, IP


a=sniff(count=1, prn=lambda x: x.show(), filter="port 53",promisc=1)
#if a[0].haslayer(DNS):
 #   print (a[0].getlayer(IP))
  #  print (a[0].getlayer(DNS))