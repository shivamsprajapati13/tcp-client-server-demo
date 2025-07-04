### 🚀 Getting Started
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


### 🔁 6. Keep Sending Queries
The client will respond with timestamps or "EMPTY" depending on the input.
You can continue sending queries until you type:
```
exit
```

### 📁 Project Structure Overview
```
folder/
├── client.py             # TCP client
├── server.py             # TCP server
├── cryptoLogic.py        # Fernet encryption/decryption helpers
└── README.md             # Instructions
```