# 🔐 Encrypted TCP Client-Server Timestamp Exchange

This project implements a TCP-based client-server system in Python that:
- Accepts string queries from a client
- Responds from the server with time-based data or an "EMPTY" response
- Encrypts all communications using Fernet symmetric encryption

- A TCP **server** listens for connections.
- A **client** connects and sends a query like `SetA-Two`.
- The server checks a predefined dictionary:
  ```python
  {
    "SetA": {"One": 1, "Two": 2},
    "SetB": {"Three": 3, "Four": 4},
    "SetC": {"Five": 5, "Six": 6},
    "SetD": {"Seven": 7, "Eight": 8},
    "SetE": {"Nine": 9, "Ten": 10}
  }

- If the value is found, server sends the current timestamp n times (where n is the value).

- If not found, server responds with "EMPTY".

#### 🔹 Encryption
- All messages between the client and server are encrypted using Fernet (from the cryptography library).

- The server supports multiple client queries in a session.

### 📁 Project Structure Overview
```
folder/
├── client.py             # TCP client
├── server.py             # TCP server
├── cryptoLogic.py        # Fernet encryption/decryption helpers
└── README.md             # Instructions
```


### 🔧 Setup & Run
Follow these steps to run the encrypted TCP client-server project:


### ✅ 1. Clone or Download the Project
```
git clone https://github.com/shivamsprajapati13/tcp-client-server-demo
```

### ✅ 2. Install Required Dependencies
Make sure Python 3.6+ is installed.

Then install the required Python package:
```
pip install cryptography
```

### 3. Start the Server
Run the server in one terminal:
```
python server.py
```

### 4. Start the Client
```
python client.py
```

You'll see a prompt:
```
Enter your Query: Eg SetA-One or type 'exit' to quit:
```
Type a query like SetA-Two to test.

### 💡 Example
### ✅ Valid input
```
Client: SetA-Two

Server:
  [CLIENT] Received: 04-07-2025 08:00:01
  [CLIENT] Received: 04-07-2025 08:00:02
```

### ❌ Invalid key
```
Client: SetZ-Unknown
Server:
  [CLIENT] Received: EMPTY
```

### 🔁 6. Keep Sending Queries
The client will respond with timestamps or "EMPTY" depending on the input.
You can continue sending queries until you type:
```
exit
```


### 🔐 Encryption Logic
- Uses Fernet from the cryptography package.

- Both client and server share the same key in secret.key.

- Messages are encrypted before sending and decrypted upon receiving.


### 📝 Notes
- You can type 'exit' in the client to close the session.

- The server sends an "END" message to let the client know it has finished responding.

- Ensure both client and server run on the same machine or allow port access across devices.

### ✅ Features Summary
 - TCP communication using sockets

 - Fernet encryption for secure transmission

 - Repeated timestamp responses from server

 - Dynamic user input with clean CLI

 - Auto key generation if missing