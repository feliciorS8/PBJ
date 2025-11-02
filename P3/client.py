import socket

# --- BAGIAN A: Otomatis membaca IP Client ---
# Dapatkan nama host lokal
hostname = socket.gethostname()
# Dapatkan IP yang sesuai dengan hostname
local_ip = socket.gethostbyname(hostname)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Alamat IP Client:', local_ip) # Tampilkan IP Client otomatis

# --- BAGIAN B: Masukkan IP dan Port Server secara dinamis ---
server_host = input('Masukkan alamat IP Server:')
# Asumsi Port juga diinput manual, atau gunakan Port default jika tidak diinput
try:
    server_port_input = input('Masukkan Port Server (default 12345):')
    server_port = int(server_port_input) if server_port_input else 12345
except ValueError:
    print("Port tidak valid. Menggunakan Port default 12345.")
    server_port = 12345
    
name = input('Masukkan username: ')

# Lakukan koneksi ke Server dengan IP/Port dinamis
clientSocket.connect((server_host, server_port))
print(f"Terkoneksi ke {server_host}:{server_port}")

# Mengirim username Client ke Server
clientSocket.send(name.encode())

# Menerima username Server
server_name = clientSocket.recv(1024).decode()
print(server_name, 'Telah bergabung...')

# --- Loop Komunikasi ---
while True:
    # 1. Mengirim pesan ke Server
    message_out = input("pesan: ")
    clientSocket.send(message_out.encode())
    
    # 2. Menerima pesan dari Server (untuk Bagian E)
    try:
        message_in = clientSocket.recv(1024)
        if not message_in:
            print("Koneksi terputus dari Server.")
            break
            
        pesan_server = message_in.decode()
        
        # Pesan dari Server sudah mengandung tanggal/jam
        print(pesan_server)
        
    except Exception as e:
        # print(f"Error menerima: {e}")
        break