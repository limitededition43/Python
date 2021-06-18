#!usr/bin/python3

import socket
from optparse import OptionParser
import sys

def findip(host):
	ip = socket.gethostbyname(host)
       	print("[%s]\t - \t[%s]" % (ip,host))

def usage():
	print("""
		[+] Usage: %s -d <target>

	Extra options:
		-d 	--domain	- domain name to be resolved
		-f	--file		- Input file containing domains""" % sys.argv[0])


try:
	parser= OptionParser()
	parser.add_option("-f", "--file", dest="filename", help="File containing domain names", action="store")
	parser.add_option("-d", "--domain", dest="domain", help="Target domain", action="store")

	(options,args) = parser.parse_args()


        if(options.domain and options.filename):
              print("\n\t[+] Please RTFM")

	elif (options.domain):
		host = options.domain
		findip(host.rstrip())

	elif(options.filename):
		file = options.filename
		with open(file) as f:
			hosts = f.readlines()
			for host in hosts:
				findip(host.strip())
	else:
		print(filename)
		usage()


except socket.gaierror:
	pass
except Exception as e:
	usage()
