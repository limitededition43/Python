import socket
from optparse import OptionParser
import sys

def findip(host):
	handler = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        ip = socket.gethostbyname(host)
        print("%s - %s" % (host,ip))

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
		findip(host)

	elif(options.filename):
		file = options.filename
		with open(file) as f:
			hosts = f.readlines()
			for host in hosts:
				findip(host.rstrip())
	else:
		usage()

except Exception as e:
	usage()
