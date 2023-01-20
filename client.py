import socket
import sys
import os
from functions import send_file, recv_file, recv_list

host = sys.argv[1]
port = sys.argv[2]
request_type = sys.argv[3]
maxfilenamelength = 40
if len(sys.argv) > 4:
        filename = sys.argv[4]
        if len(filename) > maxfilenamelength:
            print("ERROR: The filename is too long")
            exit(1)


cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv_addr = (host, int(port))

try:
    print("Connecting to " + (str(srv_addr)) + "... ")
    cli_sock.connect(srv_addr)
    print("Succesfully connected! \n")
    
    cli_sock.send(request_type.encode("utf-8"))
    print("Sending request... \n")
    
    
    
        
    if request_type == "get":
        cli_sock.send(filename.encode("utf-8"))
        recv_file(cli_sock,filename)
    elif request_type == "put":
        cli_sock.send(filename.encode("utf-8"))
        send_file(cli_sock,filename)
    elif request_type == "list":
        recv_list(cli_sock)
    else:
        print("ERROR: Please enter a valid request type")
        exit(1)
    
except Exception as e:
    print("ERROR: " + str(e))
    exit(1)

exit(0)





