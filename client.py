import socket
from cryptoLogic import encrypt_message, decrypt_message

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    while True:
        query = input("Enter your Query: Eg SetA-One or type 'exit' to quit: ").strip()
        if query.lower() == "exit":
            print("[CLIENT] Exiting.")
            break
        # print("[CLIENT] Sending Message",encrypt_message(query))
        client_socket.sendall(encrypt_message(query))

        while True:
            data = client_socket.recv(1024)
            if not data:
                print("[CLIENT] Server closed the connection.")
                exit()

            # print("[CLINET] Received Message",decrypt_message(data))
            message = decrypt_message(data)
            if message not in ("END"):
                print("[CLIENT] Received:", message)

            if message in ("END", "EMPTY"):
                break  