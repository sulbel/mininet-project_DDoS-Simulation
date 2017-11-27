import socket
import sys

# Create a server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
serv_info = ('', 10000)
sock.bind(serv_info)

while True:
    msg, addr = sock.recvfrom(4096)

    if msg:
        upperMsg = msg.upper()
        sent = sock.sendto(upperMsg, addr)
        # f = open('servResp.txt', 'w')
        # f.write(str(upperMsg))
        # f.close()


sock.close()
