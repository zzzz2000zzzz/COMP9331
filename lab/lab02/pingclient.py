from socket import *  
import time
import sys


HOST = '127.0.0.1'  
PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

  
for i in range(0,10):
    try:  
        start_time = time.time()
        clientSocket.sendto(b'A',(HOST, PORT))
        clientSocket.settimeout(1.0)
        message, address = clientSocket.recvfrom(1024)
        end_time = time.time()
        print('Ping to 127.0.0.1, seq = {}, rrt = {}ms'.format(i,int(1000*(end_time-start_time))))
    except timeout:  
        print('Resquest time out')  
