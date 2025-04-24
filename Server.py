# Este es el primer programa donde vamos a usar la libreria socket
# vamos a trabajar con el modelo cliente-Servidor


import socket  # importa la libreria socket

print("Este programa es el primer programa serevidor en python")
print("IP address:", socket.gethostbyname(socket.gethostname()))
print("Hostname:", socket.gethostname())
print("IP address:", socket.gethostbyname("www.google.com"))

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crea el socket socket.AF_INET = ipv4, socket.SOCK_STREAM = TCP
host = socket.gethostname()
port = 12345
ServerSocket.bind(("0.0.0.0", port)) # enlaza el socket con la ip y el puerto ServerSocket.bind((host, port)) # enlaza el socket con la ip y el puerto

ServerSocket.listen(5) # escucha 5 peticiones

while True: # bucle infinito
    ClientSocket, addr = ServerSocket.accept()
    print("Conexion desde: ", addr)
    msg = "Gracias por la conexion cliente de Javier" + "\r\n"
    ClientSocket.send(msg.encode("utf-8"))
    data = ClientSocket.recv(1024)
    print("Respuesta del cliente: ")
    print(data.decode("utf-8"))
    ClientSocket.close()




