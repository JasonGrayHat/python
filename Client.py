import socket
import sys

def ClientBackend():
    # Gent Instance
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Get server ip address and port from user input
    if len(sys.argv) != 3:
        print ("Correct usage: script, IP address, port number")
        exit()

    host = str(sys.argv[1])
    port = int(sys.argv[2])

    # Bind TCP client IP address and port
    client_socket.connect((host, port))
    # Take user input
    print("[*] Connection established, type any messages")
    print("[*] Type 'quit' to close connection")
    message = input("[*] Type messages: ")

    while message.lower().strip() != 'quit':
        # (1)It will simply send some text to the server
        client_socket.send(message.encode())
        # (2)and wait for the response.
        data = client_socket.recv(4096).decode()
        # Display on terminal
        print('[+] Received from server: ' + data)
        # More input
        message = input("[*] Type messages: ")
    # Close the connection
    client_socket.close()


if __name__ == '__main__':
    ClientBackend()
