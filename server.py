import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('', 12345)  # Use an empty string for the IP address to bind to all available network interfaces
server_socket.bind(server_address)

while True:
    # Receive message from client
    message, client_address = server_socket.recvfrom(1024)  # Adjust the buffer size (e.g., 1024 bytes)

    # Process the received message
    # Implement your game logic and handle the message according to your game protocol

    # Send a response back to the client if necessary
    # server_socket.sendto(response_message, client_address)

server_socket.close()
