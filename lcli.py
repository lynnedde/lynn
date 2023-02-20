#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from socket import *
import uuid

# Set the IP address and port number of the proxy server
PROXY_PORT = 1025

# Prompt the user for the destination server IP address
SERVER_IP = input("Enter the IP address of the server: ")

# Construct the HTTP request to be sent to the proxy server
REQUEST = f'GET / HTTP/1.1\r\nHost: {SERVER_IP}\r\n\r\n'

# Create a new socket object to connect to the proxy server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('', PROXY_PORT))

# Set the starting time
start_time = time.time()

# Send the HTTP request to the proxy server
clientSocket.sendall(REQUEST.encode())

# Receive the response from the proxy server
data = clientSocket.recv(4096)

# Convert the response from bytes to text
responseText = data.decode()
print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Response:\n{responseText}')

# Calculate the round-trip time
rtt = time.time() - start_time
print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - Round-trip time: {rtt:.3f} seconds')

# Get the physical MAC address of the machine
mac_address = uuid.getnode()
mac_address = ':'.join(['{:02x}'.format((mac_address >> i) & 0xff) for i in range(0, 48, 8)])

print("MAC address:", mac_address)

print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - MAC address: {mac_address}')

# Close the socket for the client
clientSocket.close()

