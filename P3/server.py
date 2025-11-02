import socket
import datetime

# Inisialisasi Socket Server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("127.0.0.1", 12345))

print("Alamat IP: 127.0.0.1")
name = input('Masukkan Username: ')

# Server menunggu koneksi
serverSocket.listen()
print("Menunggu koneksi masuk...") # Tambahan untuk feedback

# Menerima koneksi dari Client
msg, addrs = serverSocket.accept()

# --- BAGIAN C: Tanggal dan Waktu ---
# 1. Tampilkan informasi koneksi
print("Menerima koneksi dari", addrs[0])
print('Connection Established. Terkoneksi dari: ', addrs[0])

# 2. Menerima username Client
client = (msg.recv(1024)).decode()
print(client, 'telah bergabung')

# 3. Tampilkan Tanggal (Hanya sekali)
now = datetime.datetime.now()
tanggal_str = now.strftime("%d %b %Y") # Format: 01 Jul 2022
print(tanggal_str)

# 4. Kirim username Server ke Client
msg.send(name.encode())

# --- Loop Komunikasi ---
while True:
    # Cek pesan masuk dari Client
    try:
        # Menunggu pesan dari Client
        message_client = msg.recv(1024)
        if not message_client:
            print(client, "telah terputus.")
            break
            
        message_client = message_client.decode()
        
        # --- Bagian C: Tampilkan waktu (jam) pada pesan Client ---
        waktu_str = datetime.datetime.now().strftime("(%H:%M:%S)") # Format: (10:31:35)
        print(client, ':', message_client, waktu_str)

    except Exception as e:
        # print(f"Error menerima: {e}")
        break

    # --- Bagian E: Server dapat mengirimkan pesan kepada Client ---
    message_server = input("Balas pesan: ")
    
    # Tambahkan tanggal dan jam ke pesan Server
    waktu_server_str = datetime.datetime.now().strftime("(%H:%M:%S)")
    pesan_terkirim = f"{name}: {message_server} {waktu_server_str}"
    
    msg.send(pesan_terkirim.encode())