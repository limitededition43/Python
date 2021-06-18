#!usr/bin/python3


import socket
import sys

try:
	host = sys.argv[1]
	port = int(sys.argv[2])

#Create socket object

	handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 	#tcp connection
								   	#Establish connection
	print("Connecting to : " , host , port)

	handler.connect((host,port))
									#sending data

	handler.send("Hello from client")
									#receive response

	response = handler.recv(4096)


	print(response)

except Exception as e :
	print ("[+] Usage: %s <host> <port>" % sys.argv[0])
	print e
