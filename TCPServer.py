#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname
port = 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("received connection from  " % str(address))

    message = 'THANK YOU FOR CONNECTING TO THE SERVER!' + "\r\n"

    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()
