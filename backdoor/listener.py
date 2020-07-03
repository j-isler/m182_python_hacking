#!/usr/bin/env python

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # allows to reuse the socket
listener.bind(("192.168.1.247", 4444))
listener.listen(0)
