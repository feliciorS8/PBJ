import socket
import threading
import datetime # Tambahkan modul datetime

userName = input("Masukkan username: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Sesuaikan dengan host dan port Server
host_server = '127.0.0.1'
port_server = 55555
client.connect((host_server, port_server))

# Variabel untuk melacak apakah tanggal sudah ditampilkan
tanggal_ditampilkan = False

# Fungsi untuk menerima pesan dari Server secara asinkron
def receive():
    global tanggal_ditampilkan
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                # Mengirim username sebagai respons NICK
                client.send(userName.encode('ascii'))
            else:
                # --- Bagian A & B: Menambahkan Tanggal dan Waktu ke Output ---
                
                # 1. Tampilkan Tanggal (Hanya sekali per sesi)
                if not tanggal_ditampilkan:
                    now = datetime.datetime.now()
                    tanggal_str = now.strftime("%d %b %Y")
                    print(tanggal_str)
                    tanggal_ditampilkan = True
                    
                print(message)
                
        except:
            # Jika terjadi error
            print("Terjadi kesalahan atau koneksi terputus!")
            client.close()
            break

# Fungsi untuk mengirim pesan ke Server secara asinkron
def write():
    while True:
        # Mengambil input pesan dari user
        pesan_raw = input('>>')
        
        # --- Bagian B: Tambahkan Waktu Pengiriman ---
        now = datetime.datetime.now()
        waktu_str = now.strftime("(%H:%M:%S)")
        
        # Format pesan: "nickname: pesan (HH:MM:SS)"
        # Note: Kita harus memisahkan pesan dari nickname
        message = f"{userName}: {pesan_raw} {waktu_str}"
        
        try:
            client.send(message.encode('ascii'))
        except:
            print("Gagal mengirim pesan. Koneksi terputus.")
            break

# --- Threading untuk komunikasi simultan ---
# Thread untuk menerima pesan
receive_thread = threading.Thread(target=receive)
receive_thread.start()

# Thread untuk mengirim pesan
write_thread = threading.Thread(target=write)
write_thread.start()