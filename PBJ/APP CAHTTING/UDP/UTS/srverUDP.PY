import socket

# Konfigurasi server
ip_server = "192.169.2.1"
port_server = 5005
buffer_size = 1024

# Buat UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((ip_server, port_server))

print(f"Server UDP berjalan di {ip_server}:{port_server}")

while True:
    data, addr = server_socket.recvfrom(buffer_size)
    print(f"Pesan dari {addr}: {data.decode()}")

    # Balas pesan ke client
    balasan = input("Balas ke client: ")
    server_socket.sendto(balasan.encode(), addr)
