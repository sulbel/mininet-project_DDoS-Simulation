import socket
import sys

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.0.0.1', 10000)
message = 'junk ' #* 600

for i in xrange(20):
    # Send data
    sent = s.sendto(message, server_address)

    # Receive response
    data, server = s.recvfrom(4096)

    # debugging -
    # f = open('clientResp.txt', 'w')
    # f.write(str(data))
    # f.close()


s.close()
sys.exit()
