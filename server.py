import json
import socket
import threading
import os
import hashlib


def handle_client(client_socket):
    request = client_socket.recv(1024)
    request = request.decode()
    print(f"[*] Received: {request}")
   

    try:
        with open("messages.json", "r") as f:
            datalist=json.load(f)
            for item in datalist:
                value = item.get("value")
                hash_value = item.get("hash_value")
            
            
            
           
    except FileNotFoundError:
        print("heleo")
        hash_msg="abdulhammad"
        sha256 = hashlib.sha256()
        sha256.update(hash_msg.encode())
        hash_value = sha256.hexdigest()
        value=0
        datalist = []
    
    
    try:
        value+=int(request)
      
        with open("messages.json", "w") as f:
            sha256 = hashlib.sha256()
            sha256.update(hash_value.encode())
            hash_value = sha256.hexdigest()
            data = {
                "value" : value,
                "hash_value" : hash_value
                }
            datalist.append(data)
            json.dump(datalist, f)
           
    except FileNotFoundError:
        print("filenotopened")
      
   
    client_socket.send(b"ACK!")
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 1234))
server.listen(5)
print("[*] Listening on 0.0.0.0:1234")

while True:
    client, addr = server.accept()
    print(f"[*] Connection from {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()