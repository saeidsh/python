from scapy.all import Ether, ARP, srp

broadcast="FF:FF:FF:FF:FF:FF"
ip_range="192.168.2.1/24"
arp_layer=ARP(pdst=ip_range)
ether_layer=Ether(dst=broadcast)
packet=ether_layer/arp_layer

ans, unans =srp(packet,iface="enp1s0f0",timeout=2)

for snd, rcv in ans:
    ip= rcv[ARP].psrc
    mac=rcv[Ether].src
    print("IP = ",ip,"MAC = ",mac)
