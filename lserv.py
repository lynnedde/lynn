#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
from time import *


# Set the port number that the proxy server will listen on
serverPORT = 1025

# Create a new socket object to listen for incoming connections on the specified port
# and bind it to the local machine's network interface
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPORT))

# Begin listening for incoming connections
serverSocket.listen(1)

# Print a message to indicate that the server is running and listening on the specified port
start_time = time()
print(f"[{strftime('%Y-%m-%d %H:%M:%S')}] Proxy server running on port {serverPORT}")

# Loop forever, waiting for incoming connections
while True:
    # Wait for a client to connect and accept the connection
    clientSocket, client_address = serverSocket.accept()

    # Print a message to indicate that a client has connected
    print(f"[{strftime('%Y-%m-%d %H:%M:%S')}] Connection from {client_address[0]}")

    # Receive the client's HTTP request and decode it from bytes to text
    requestData = clientSocket.recv(4096)
    requestText = requestData.decode('utf-8')

    # Print a message to indicate that the request has been received
    print(f"[{strftime('%Y-%m-%d %H:%M:%S')}] Received request from client")

    # Extract the destination server's IP address from the client's HTTP request
    host_start = requestText.find('Host: ') + 6
    host_end = requestText.find('\r\n', host_start)
    server_host = requestText[host_start:host_end]

    # Create a new socket object to connect to the destination server on port 80 (the default HTTP port)
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.connect((server_host, 80))

    # Forward the client's HTTP request to the destination server
    serverSocket.sendall(requestData)

    # Receive the response from the destination server

    data = serverSocket.recv(4096)

    # Forward the response from the destination server back to the client
    clientSocket.send(data)

    # Print a message to indicate that the response has been sent back to the client
    print(f"[{strftime('%Y-%m-%d %H:%M:%S')}] Sent response back to client.")

    # Close the sockets for the client and destination server
    clientSocket.close()
    serverSocket.close()
