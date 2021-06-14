# Networking using Python  


## Creating client and server using socket.  
	
	TCP 	 = socket.SOCK_STREAM  
	UDP 	 = socket.S0CK_DGRAM  	
	AF_INET4 = IPV4 address  
	AF_INET6 = IPV6 address  

# Client  

##### Creating a TCP socket  

	s = socket.socket(socket.AF_INET4, socket.SOCK_STREAM)  

##### Creating a UDP socket

	s = socket.socket(socket.AF_INET4, socket.SOCK_DGRAM)

##### Establishing TCP connection to target 
	
	s.connect((host,port))  

##### Esatablish UDP connection to target

	UDP is connection less. Data can be sent without establishing a connection. 

##### TCP send data to target
	
	s.send("message")  

##### UDP send data to target
	
	s.sendto("message",(host,port))

##### TCP receive data from target  
	
	response = s.recv(1024)  

##### UDP receive data from target  

	client, addr = s.recvfrom(1024)  
	

# Server:

##### Bind to listening ip and port
	
	s.bind((listen_ip,listen_port))  

##### Listening on bind address

	s.listen(5)  

##### Close connection

	s.close()

