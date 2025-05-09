import socket
from threading import Thread  #menerima pesan dari client lain

SERVER_HOST = "192.168.22.201" #sebuah alamat ip
SERVER_PORT = 5002
separator_token = "<SEP>"#un memisahkan nama pengguna degn chat
#client_socket:s = socket.socket(untuk meyimpan elemen unik yang digunakan menyimpan semua objek dari client yang terhubung)
client_sockets = set()
#S.SOCKET.SOCKET(ini adalah socket TCP/IP karena TCP meneyediakan komunikasi yang handal dan berurutan)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#SO_REUSEADOR Mengizinkan penggunaan kembali alamat dan port yang sama segera setelah server ditutup atau mengalami crash. Tanpa opsi ini, sistem operasi mungkin menahan port untuk sementara waktu.
s.bind((SERVER_HOST, SERVER_PORT))
#s.bind Variabel yang digunakan untuk mengikat alamat IP dan port ke socket server. 
s.listen(5)
#s.listen Mendengarkan koneksi masuk dari klien. Angka 5 menunjukkan jumlah maksimum koneksi yang dapat diterima pada satu waktu.

print(f"[*] Server listening as {SERVER_HOST}:{SERVER_PORT}")
#mencetak pesan keserver untuk infoin bahwa server berhasil diinisialisasi dan sedang mendengarkan koneksi pada alamat ip dan port yang ditentukan

def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Client disconnected: {e}")
            client_sockets.remove(cs)
            cs.close()
            break                                                                                                                                                                                                                                                                                                             
        else:
            for client in client_sockets:
                if client != cs:
                    try:
                        client.send(msg.encode())
                    except Exception as e:
                        print(f"[!] Error sending message: {e}")

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,))
    t.start()