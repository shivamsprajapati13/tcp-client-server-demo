import socket
from datetime import datetime
import time
from cryptoLogic import encrypt_message, decrypt_message

data = {
    "SetA": {"One": 1, "Two": 2},
    "SetB": {"Three": 3, "Four": 4},
    "SetC": {"Five": 5, "Six": 6},
    "SetD": {"Seven": 7, "Eight": 8},
    "SetE": {"Nine": 9, "Ten": 10}
}

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[SERVER] Listening on {HOST}:{PORT}...")

    conn, addr = server_socket.accept()
    with conn:
        print(f"[SERVER] Connected by {addr}")
        while True:
            data_received = conn.recv(1024)
            # print("[SERVER] Received Message from Client--->",data_received)
            if not data_received:
                break

            try:
                decrypted = decrypt_message(data_received) 
                print(f"[SERVER] Decrypted message: {decrypted}")

                set_name, key = decrypted.strip().split('-')
                subset = data.get(set_name)

                if subset and key in subset:
                    n = subset[key]
                    for _ in range(n):
                        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        # print("[SERVER] Encrypted Message",encrypt_message(current_time))
                        conn.sendall(encrypt_message(current_time))  
                        time.sleep(1)
                    conn.sendall(encrypt_message("END"))
                else:
                    conn.sendall(encrypt_message("EMPTY"))

            except Exception as e:
                print(f"[SERVER] Error: {e}")
                conn.sendall(encrypt_message("EMPTY")) 
