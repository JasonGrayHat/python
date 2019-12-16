import socket
import logging

# (4)Logging format
logging.basicConfig(filename="socket.log", level=logging.DEBUG, format="%(asctime)s:%(levelname)s:%(message)s ")


def ServerBackend():
    host = "127.0.0.1"
    port = 4444
    # Get Instance
    server_socket = socket.socket()
    # Bind TCP host IP address and port
    server_socket.bind((host, port))
    logging.debug("Server started: {} ({})".format(host, port))
    # Maximum number of clients
    server_socket.listen(2)
    # Accept New connetions
    conn, address = server_socket.accept()
    logging.debug("Connected from: {}".format(str(address)))
    print("[*] Connection initiated from: " + str(address))
    print("[*] Ready to accept incoming connections")
    while True:
        # (1)Receive text from the client with amount of packet limit
        data = conn.recv(4096).decode()
        # If nothing is transmitted, break
        if not data:
            break

        print("[+] From client: " + str(data))
        logging.debug("From Client: {}".format(str(data)))
        # (2)Change it to all uppercase, (3)then send it back.
        conn.send(data.upper().encode())
        print("[*] Echoed to client: " + str(data.upper()))
        logging.debug("To Clint: {}".format(str(data.upper())))

    # Close the connection
    conn.close()
    logging.debug("Connection closed")


if __name__ == '__main__':
    ServerBackend()
