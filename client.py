import socket

def dns_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(200)  # Set a timeout for receiving the response
    client_socket.connect((server_ip,server_port))
    query = "www.google.com"

    client_socket.sendto(query.encode(), (server_ip, server_port))


    while True:

        response = client_socket.recvfrom(1024)
        print("Received data from server:{}",format(response.decode()))


        client_socket.close()


server_ip = '127.0.0.5'
server_port = 1234
dns_client(server_ip, server_port)

