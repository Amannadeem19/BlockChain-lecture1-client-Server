# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:56:12 2023

@author: STUDENT
"""


#hashed code

import socket
import json
import hashlib


while True:
    
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.103", 1234))
    
    val=100
    
    message = input("Enter your message: ")
    
    # Generate the hash value using SHA-256
    hash_msg  = 'abubakr'
    sha256 = hashlib.sha256()
    sha256.update(hash_msg.encode())
    hash_value = sha256.hexdigest()
    print(hash_value)
    
    #read the json content
    try:
        with open("messages2.json", "r") as f:
            datalist = json.load(f)
            for item in datalist:
                val = item.get("remaining_value")
                hash_value = item.get("hash_value")
            
          
    except FileNotFoundError:
        print("file not opened for reaad")
        datalist = []
    
    
    # save the json data
    try:
    
        
        
        
      if val <= 0:
          print("your balance is not enough")
          
            
      else:
          
          
          val-=int(message)
          
          with open("messages2.json","w") as f:
              
              
              print("remaining " ,val)
              sha256 = hashlib.sha256()
              sha256.update(hash_value.encode())
              hash_value = sha256.hexdigest()
              print(hash_value)
              data={"remaining_value": val, "hash_value": hash_value}
              datalist.append(data)
             
              json.dump(datalist, f)
              client.send(message.encode())
    except FileNotFoundError:
        print("filenotfound")
          
           
      
    
       
    
    
        
    
    response = client.recv(1024)
    print(response)
    client.close()