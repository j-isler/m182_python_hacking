#!/usr/bin/env python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # allows to reuse the socket
listener.bind(("192.168.1.113", 4444))  # bind socket to our computer to listen to connections to port
listener.listen(0)
print("[+] Waiting for incoming connections.")
connection, address = listener.accept()
print("[+] You've got a connection!" + str(address))
