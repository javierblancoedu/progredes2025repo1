import socket  # importa la libreria socket

print("Este programa es el primer programa cliente en python")

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # crea el socket socket.AF_INET = ipv4, socket.SOCK_STREAM = TCP
#host = socket.gethostname()
host = "127.0.0.1"
port = 12345
ClientSocket.connect((host, port))

msg = "Gracias por la conexion soy el cliente" + "\r\n"
ClientSocket.send(msg.encode("utf-8"))
data = ClientSocket.recv(1024) # recibe 1024 bytes
print("Respuesta del servidor: ")
print(data.decode("utf-8"))
ClientSocket.close()