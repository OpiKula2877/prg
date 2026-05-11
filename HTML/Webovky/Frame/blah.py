import socket

target_ip = "192.168.68.175"
target_port = 8000

# Hikvision SDK HELLO paket (zjednodušený)
# Toto je pokus o vyvolání odpovědi z portu 8000
buffer = bytearray([0x03, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00])

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect((target_ip, target_port))
    s.send(buffer)
    data = s.recv(1024)
    print(f"Odpověď z portu 8000 (hex): {data.hex()}")
    s.close()
except Exception as e:
    print(f"Chyba spojení: {e}")