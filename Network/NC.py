#!/usr/bin/python

import sys
import socket
import getopt
import threading
import subprocess

# gloabl variables

listen = False
command = ''
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0


def usage():
    print '\n\tRTFM'


def server_loop():
    global target

    if not len(target):
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        (data, addr) = server.accept()
        client_thread = threading.Thread(target=client_handler,args=(data, ))
        client_thread.start()


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))

        if len(buffer):
            print 'Sending buffer'
            client.send(buffer)

        while True:
            recv_len = 1
            response = ''

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data
                if recv_len < 4096:
                    break
            print response
            buffer = raw_input('')
            buffer = '\n'
            client.send(buffer)
    except:

        print '[+] Exiting '
        client.close()


def run_command():
    command = command.rstrip()
    try:
        output = os.system(command)
    except:

        output = 'Failed to execute command'

    return output


def client_handler(data):
    global upload
    global execute
    global command

    if len(upload_destination):
        file_buffer = ''

        while True:
            data = client_sender.recv(1024)
            if not data:
                break
            else:
                file_buffer += data

            try:
                file_descriptor = open(upload_destination, 'wb')
                file_descriptor.write(file_buffer)
                file_descriptor.close()

                client_sender.send('Successfully saved to file %s '
                                   % upload_destination)
            except:

                client_sender.send('Failed to save file to %s'
                                   % upload_destination)

    if len(command):
        output = run_command()
        client_sender.send(output)

        while True:
            client_sender.send('stupid-machine:#')
            cmd_buffer = ''

            while '\n' not in cmd_buffer:
                cmd_buffer += client_sender.recv(1024)
                response = run_command(cmd_buffer)

                client_sender.send(response)


def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:

        # get opt argument parser

        (options, arguments) = getopt.getopt(sys.argv[1:], 'hle:t:p:cu:'
                , [
            'help',
            'listen',
            'execute',
            'target',
            'port',
            'command',
            'upload',
            ])
    except getopt.GetoptError, err:
        print err
        usage()

    for (o, a) in options:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-l', '--listen'):
            listen = True
        elif o in ('-e', '--execute'):
            execute = a
        elif o in ('-c', '--command'):
            command = a
        elif o in ('-u', '--upload'):
            upload_destination = a
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, 'Unhandled Option'

    if not listen and len(target) and port > 0:
        print 'Connecting'
        buffer = sys.stdin.read()
        client_sender(buffer)  # This function send the user input through stdin

    if listen:
        server_loop()  # This will start the server_loop listener function


main()

