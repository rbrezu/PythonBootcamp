import socket

host = ''        # Symbolic name meaning all available interfaces
port = 1234     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)
conn, addr = s.accept()

print('Connected by', addr)
while True:
    data = conn.recv(1024)

    print (data.decode('utf-8').split(' '))
    if not data: break
    conn.sendall(data)

conn.close()