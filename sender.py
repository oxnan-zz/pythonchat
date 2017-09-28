# Send

# Let's say this code is executed from PC1.

import socket

UDP_IP = 'localhost' # IP address is not valid, it is just for example.
UDP_PORT = 5005
MESSAGE = "Hey there!"


sock = socket.socket(socket.AF_INET,
             socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
