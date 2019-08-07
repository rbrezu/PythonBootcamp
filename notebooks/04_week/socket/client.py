import socket

host = socket.gethostname()
port = 1234                # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    message = input('Write to server:\n')
    if message == 'q':
        break

    s.sendall(message.encode('utf-8'))

    data = s.recv(1024)
    print (data)

s.close()
print('Received', repr(data))