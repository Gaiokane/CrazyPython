import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 调用connect连接服务端
client_socket.connect(("192.168.1.55", 30000))

# 一旦建立连接之后，server与client虚拟链路建立成功
print(client_socket.recv(2048).decode('UTF-8'))