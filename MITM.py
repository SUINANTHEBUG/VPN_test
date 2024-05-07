from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        ip_layer = packet[IP]
        tcp_layer = packet[TCP]
        print(f"IP: {ip_layer.src} -> {ip_layer.dst}")
        print(f"TCP: {tcp_layer.sport} -> {tcp_layer.dport}")
        if tcp_layer.payload:
            original_data = tcp_layer.payload.load
            new_data = original_data.replace(b'original', b'modified')
            print(f"Original Data: {original_data}")
            print(f"Modified Data: {new_data}")
def start_sniffing(target_ip):
    print(f"Starting to sniff on IP: {target_ip}")
    sniff(filter=f"ip host {target_ip}", prn=packet_handler, store=False)
start_sniffing('192.168.1.5')
