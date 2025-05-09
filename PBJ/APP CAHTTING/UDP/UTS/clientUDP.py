import socket

# Konfigurasi server tujuan
ip_server = "192.168.2.1"
port_server = 5002
buffer_size = 1024

# Buat UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Ketik 'exit' untuk keluar")

while True:
    pesan = input("Kirim ke server: ")
    if pesan.lower() == 'exit':
        break

    # Kirim pesan ke server
    client_socket.sendto(pesan.encode(), (ip_server, port_server))

    # Terima balasan dari server
    data, addr = client_socket.recvfrom(buffer_size)
    print(f"Balasan dari server: {data.decode()}")

client_socket.close()
