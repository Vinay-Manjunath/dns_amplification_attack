import socket

MAX_QUERIES=10

def dns_server():

    dns_table = {"www.google.com":"192.165.1.1",

    "www.youtube.com":"192.165.1.2",

    "www.python.org":"192.165.1.3", "www.aurcc.ac.in":"192.165.1.4",

    "www.amazon.in":"192.165.1.5",

    "www.gmail.com":"192.165.1.6"}

    ip_client = '127.0.0.5'
    port_client = 1234
    ip_attack='127.0.0.2'
    port_attack=4321

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.bind((ip_client, port_client))

    attack_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    attack_socket.bind((ip_attack, port_attack))


    print("DNS server started ")

    query_counter=0

    while True:
        data, addr = attack_socket.recvfrom(1024)
        print("Received DNS query from {}:{}".format(addr[0], addr[1]))

        query_counter+=1

        if query_counter>MAX_QUERIES:
            print("Query limit reached: Ignoring further queries.")
            break


       # if addr[0]=='127.0.0.1':
        response_data= dns_table.get(data, "Not Found!").encode()
        client_socket.sendto(response_data, (ip_client,port_client))
    
       # if addr[0]=='127.0.0.2':
        #    response_data=ip = dns_table.get(data, "Not Found!").encode()
         #   client_socket.sendto(response_data, addr)


if __name__ == '__main__':
    dns_server()

