#coding:utf-8
from socket import *

host = '127.0.0.1'   
port =  9999 
address = (host, port)
serverSocket = socket(AF_INET, SOCK_STREAM) 
serverSocket.bind(address)  
serverSocket.listen(1)  

while True:
    try:
        connectionSocket, clientAddr = serverSocket.accept()   
        message = connectionSocket.recv(1024)   
        filename = message.split()[1]   
        f = open(filename[1:].decode('ascii'))
        outputdata = f.readlines() 
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode('ascii'))   
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode('ascii'))   
        connectionSocket.close()    
    except IOError:
        connectionSocket.send("404 not found".encode('ascii'))  
        connectionSocket.close()
serverSocket.close()
