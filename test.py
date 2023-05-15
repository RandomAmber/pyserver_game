import socket

def play_game(connection):
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break
        
        print("Received:", data)
        guess = input("Enter your guess: ")
        connection.send(guess.encode())

# Server code
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8888))
    server_socket.listen(1)
    
    print("Waiting for connections...")
    connection, address = server_socket.accept()
    print("Connected to:", address)
    
    play_game(connection)
    
    connection.close()
    server_socket.close()

# Client code
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8888))
    
    play_game(client_socket)
    
    client_socket.close()

# Main entry point
if __name__ == '__main__':
    mode = input("Enter 'server' to run as server or 'client' to run as client: ")
    
    if mode == 'server':
        run_server()
    elif mode == 'client':
        run_client()
    else:
        print("Invalid mode. Please enter 'server' or 'client'.")
