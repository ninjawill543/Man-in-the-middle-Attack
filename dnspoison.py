from scapy.all import sniff


a=sniff(filter="port 53",count=1,promisc=1)
print(a[0])
  