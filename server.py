import socket
import sys
from functions import send_file, recv_file, send_list

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "0.0.0.0"
port = sys.argv[1]

try:
    srv_sock.bind((host, int(port)))
    print("\n Server up and running on IP: "+ host + " and port: " + port + "\n")
    srv_sock.listen(5)
    
except Exception as e:
    print("Error:" + str(e))
    exit(1)

    
    
while True:

    try:
        print("Waiting for new client... \n")
        cli_sock, cli_addr = srv_sock.accept()
        str_cli_addr = (str(cli_addr))
        print("Client " + str_cli_addr + " connected. \n")
        
        request_type = cli_sock.recv(1024).decode("utf-8")
        print("Request recieved from client: " + request_type + "\n")
        
        
        if request_type == "get":
            filename = cli_sock.recv(1024).decode("utf-8")
            print("Filename: " + filename + "\n")
            send_file(cli_sock, filename)

        elif request_type == "put":
            filename = cli_sock.recv(1024).decode("utf-8")
            print("Filename: " + filename + "\n")
            recv_file(cli_sock, filename)

            
        elif request_type == "list":
            try:
                send_list(cli_sock)
            except Exception as e:
                print("Error:" + str(e))
                exit(1)
        else:
            print("Error: Incorrect request type")
            
            
            
    finally:
        print("Disconnecting from client.... ")
        try:
            cli_sock.close()
            print("Succesfully disconnected! \n")
        except Exception as e:
            print("Error" + str(e))

        


srv_sock.close()

exit(0)