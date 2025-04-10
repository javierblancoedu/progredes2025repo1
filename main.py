import socket

print("IP address:", socket.gethostbyname(socket.gethostname()))
print("Hostname:", socket.gethostname())

print("IP address:", socket.gethostbyname("www.google.com"))
print("Hostname:", socket.gethostname())

