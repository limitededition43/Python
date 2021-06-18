#!usr/bin/python3

import socket
import sys

try:
	host = str(sys.argv[1])
	port = int(sys.argv[2])

#Create socket object

	handler = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 	#udp connection - SOCK_DGRAM

	print("UDP connectionless: ")					#No connection neeted

	handler.sendto('Hello',(host,port))		#UDP is connectionless, data can be sent directly using sendto()

	data, addr = handler.recvfrom(4096)				#receive response using recvfrom()

	print(data)

except Exception as e :
	print ("[+] Usage: %s <host> <port>" % sys.argv[0])
