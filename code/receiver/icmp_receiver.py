from scapy.all import ICMP, IP, sniff

def receive_packet(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1:
        packet.show()


sniff(filter="icmp", prn=receive_packet)

