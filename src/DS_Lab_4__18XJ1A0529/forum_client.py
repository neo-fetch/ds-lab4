import socket
import time
import os
from tqdm import tqdm
import _thread


HOST = '127.0.0.1'
PORT_S = 9090
# PORT_S = 8080

client_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_skt.connect((HOST,PORT_S)) # change HOST to the IP of the server you want to send text to

def servermsgs():
    while True:
            msg = client_skt.recv(1024).decode('utf-8')
            if not msg:
                break
            print(msg)

_thread.start_new_thread(servermsgs, ( ))
print("Enter message and the client number separated by a \':\'\nFor example: 2:message sends \'message\' to User2) or \'/quit\' to exit:\nEnter \'/join\' to subscribe to multicast alerts")

while True:
    
    msg = input()
    msgcpy = msg
    if msg == "/join":
        print("You have successfully joined the multicast group.\n To send a message to the group, type \'cast\' instead of the client number.\n For example:\ncast:message sends \'message\' to everyone subscribed to the multicast group")
        
    msg=msg.encode("utf-8")
    client_skt.sendall(msg)
    if msgcpy == "/quit":
        quit()
