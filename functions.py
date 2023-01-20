import os
import socket


def send_file(sock,filename):
    print("Attempting to upload " + filename + "....")
    with open(filename, 'rb') as f:

        filedata = f.read(1024)
        sock.sendall(filedata)
        
    print("Sent succesfully!")
    sock.close()
    
def recv_file(sock,filename):
    print("Attempting to download " + filename + "....")
    filedata = (sock.recv(1024))
    
    with open(filename, 'xb') as f:
        datarecieved = len(filedata)
        print(datarecieved)
        f.write(filedata)
        while not filedata:
            filedata = sock.recv(1024)
            f.write(filedata)
    print("Recieved succesfully!")
    sock.close()

                              
def send_list(sock):
    print("Generating list of directories...")
    directory_list = os.listdir()
    try:
        sock.sendall(str(directory_list).encode("utf-8"))      #converted the list into string and then into bytes to send across socket
        print("List sent succesfully")
    except Exception as e:
        print("Error: " + e)
    sock.close()                             
                              
                              
                              
def recv_list(sock):
    print("Requesting list of directories...")
    str_directory_list = sock.recv(1024).decode("utf-8")
    directory_list = eval(str_directory_list)                   #converted the str of lists back to a list
    print("List recieved succesfully \n")
    
    for file in directory_list:
        print(file)
        
    sock.close()
    
