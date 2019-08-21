import socket

target_host = "www.google.com"

target_port = 80  # create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
client.send(request.encode())

# receive some data
buffer = b''
while True:
    response = client.recv(2048)
    buffer += response
    if len(response) < 2048:
        break

http_response = repr(buffer)
http_response_len = len(buffer)

#display the response
print("[RECV] - length: %d" % http_response_len)
print(http_response)


## You can write that or this:

import requests
print (requests.get('http://www.google.ro').content)
