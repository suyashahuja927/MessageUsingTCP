# TCPSockets
A python application to transfer messages/images/files using TCP sockets.


TCP uses the 3-way-handshake method
to connect.
TCP protocol is a low-level transport protocol, and it exchanges data using binary. The
presentation layer takes control of the encoding of the strings into bytes so they can pass
through the sockets. It uses the encoding type “utf-8” throughout. This can be then
decoded on the other side. It uses a binary scheme as TCP is a low-level transport protocol.
The application layer is useful for printing all the statements like “server up and running on
IP: …”, and this is very important as it keeps the user and server user updated on if their
program is functioning as required.
My solution tries to use “try” statements wherever possible, this is to ensure that if there is
an error, it can be printed out on the screen, and it will be easier for the client/user to
understand.
This solution also uses a 3
rd python file called “functions.py” which has a variety of abstract
functions which were common for both server and client side. Although, if you want to run
the files from different directories to allow uploading/downloading files with the same
name, you will have to copy the functions.py to both the directories.
As required, it takes in the arguments from the command prompt using sys.argv which
allows users to give arguments from the start. It also assumes that the maximum length of a
filename shouldn’t be more than 15chars, although this can be changed easily. It also checks
the request type and makes sure it is one of “get”,” put”, or “list”.
After every request, the session layer from the server disconnects from the clients socket
and it allows other clients to join in. Multiple clients at one point is not supported by this
solution as that would require threading. The session layer is important to ensure
connections between the TCP sockets as it co-ordinates the connections.
For the “list” request type, os.listdir() returns a list, and it is not possible to pass through an
array through sockets unless you convert it using array.tobytes() or anything similar. For my
solution, I decided to convert the array into a string and then encode it using “utf-8” which
can then again be decoded on the client side and converted back to a list using eval
function.
