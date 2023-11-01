import socket

target_ip = "127.0.0.2"

def send_dns_query():

    query = "www.google.com"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((target_ip, 4321))
    sock.sendto (query.encode(),(target_ip, 4321))
    sock.close()

if __name__ == '__main__':
    query_count = 100       # Number of queries to send

    for _ in range(query_count):
        send_dns_query()

