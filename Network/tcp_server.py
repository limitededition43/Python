import socket
import sys
import threading

try:

	listen_ip= str(sys.argv[1])
	listen_port = int(sys.argv[2])

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	#Create TCP socket

	server.bind((listen_ip,listen_port))				#bind to listening ip and port

	server.listen(5)						#Start the listener of maximum connection backlog of 5

	print("[+] Listening on %s:%d" % (listen_ip,listen_port))	#Displaying cool message

	#Create a function to handle incoming client

	def client_handle(handler):
		request = handler.recv(1024)				#recv data from handler object
		print("[+] Received : %s" % request)			#Print the request from client

		handler.send("Got ya!")					#Send an acknowledgment to client

		handler.close()

	while True:							#This will run our server forever

		client, addr = server.accept()				#Accepting incoming connection
		print (addr)
		print (client)
		print("[+] Connection from %s:%d ." % (addr[0],addr[1]))	#Print the addr details of client


		client_handler_thread = threading.Thread(target=client_handle,args=(client,))	#Create a thread to handle 
		client_handler_thread.start()


except Exception as e:
	print("[+] Usage : %s <listen_ip> <listen_port> " % sys.argv[0])
