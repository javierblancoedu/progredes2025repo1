import socket

print("Este programa es el priemro en python")
print("IP address:", socket.gethostbyname(socket.gethostname()))
print("Hostname:", socket.gethostname())

print("IP address:", socket.gethostbyname("www.google.com"))
print("Hostname:", socket.gethostname())


