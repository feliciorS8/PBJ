import socket
import threading
import datetime # Tambahkan modul datetime

# Inisialisasi Socket Server
host = '127.0.0.1'
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Output status Server aktif (Sesuai contoh)
print("Server telah aktif...")

# Fungsi untuk mengirim pesan ke semua Client yang terhubung
def broadcast(message):
    for client in clients:
        client.send(message)

# Fungsi untuk menangani koneksi dari Client tertentu
def handle(client):
    while True:
        try:
            # Menerima pesan (sudah termasuk nickname, pesan, dan waktu/tanggal dari Client)
            message = client.recv(1024)
            
            # Server tidak perlu memodifikasi pesan, cukup me-broadcast pesan
            # yang sudah diformat oleh Client
            broadcast(message)
        except:
            # Menghapus Client jika terjadi error atau koneksi terputus
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            
            # Menyiapkan pesan keluar
            # Sesuai contoh, pesan keluar tidak perlu tanggal/waktu, cukup notifikasi
            pesan_keluar = '{} keluar!'.format(nickname).encode('ascii')
            broadcast(pesan_keluar)
            nicknames.remove(nickname)
            break

# Fungsi untuk menerima koneksi baru
def receive():
    while True:
        client, address = server.accept()
        
        # --- Modifikasi Output Sesuai Soal ---
        # Tampilkan alamat dan port Client yang terhubung (Sesuai contoh)
        print(f"User user {len(clients) + 1} telah bergabung pada {str(address)}")

        # Meminta username dari Client
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Username {nickname}")
        
        # Mengirim notifikasi ke Client baru
        client.send('Terkoneksi dengan Server!'.encode('ascii'))
        
        # Mengirim notifikasi bergabung ke semua Client
        broadcast(f"{nickname} Bergabung!".encode('ascii'))

        # Membuat thread baru untuk menangani Client ini
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Memulai fungsi penerimaan koneksi
receive()