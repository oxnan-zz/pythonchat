import socket

ip =  "localhost"

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((ip, 5005))



while True:
    data, addr = udp.recvfrom(1024)
    print data
    UDP_IP = 'localhost' # IP address is not valid, it is just for example.
    UDP_PORT = 5005
    MESSAGE = "Hey there!"


    sock = socket.socket(socket.AF_INET,
                 socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
