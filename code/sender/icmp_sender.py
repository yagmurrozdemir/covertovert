from scapy.all import ICMP, IP, send

packet = IP(dst="receiver") / ICMP()

packet.ttl = 1 

send(packet)
