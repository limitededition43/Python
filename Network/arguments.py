
import getopt
import sys


global listen
global target
global port
global command


listen = False
port = 0
target = ""
command = ""




def main():
        if not listen and len(target) and port > 0 :
                print("Connecting to %s:%s" %(target,port))
        	if len(command):
                	print("Executing command : %s" % command)
 	elif listen and port>0 and not len(command):
		print("Listening on 0.0.0.0:%s" % port)
	else:
		usage()

def usage():
  print("Please RTFM")


if not len(sys.argv[1:]):
      usage()

try:
  opts , args = getopt.getopt(sys.argv[1:],"lt:p:c:",["listen","target","port","command"])

  for o,a in opts:
    if o in ("-l"):
	listen = True

    elif o in ("-t"):
	target = a

    elif o in ("-p"):
    	port = a

    elif o in ("-c"):
	command = a

except getopt.GetoptError as e:
    print(str(e))

except:
	usage()
	print("mew")


main()
