
import socket
import argparse

parser = argparse.ArgumentParser(description='Process args.')
parser.add_argument('-p', '--port', help='DNS server port', required=True, type=int)
args = parser.parse_args()
dns_port = args.port

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# DNS LISTENER ON SPECIFIED PORT
listen_on = ("", dns_port)
udp_socket.bind(listen_on)

while True:
    data, source = udp_socket.recvfrom(1024)
    print(data.strip().decode('utf-8'))
