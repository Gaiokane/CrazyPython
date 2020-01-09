import socket
import threading


def read_server(client_socket):
    # 一旦建立连接之后，server与client虚拟链路建立成功
    while True:
        content = client_socket.recv(2048).decode('UTF-8')
        if content is not None:
            print(content)


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 调用connect连接服务端
client_socket.connect(("192.168.1.55", 30000))
# 将read_server函数以多线程的方式启动，这样该函数（包含死循环）能与下面的死循环并发执行
threading.Thread(target=read_server, args=(client_socket,)).start()
while True:
    # 获取用户输入
    line = input('')
    if line is None or line == 'exit':
        break
    # 将用户输入的内容写入王略
    client_socket.send(line.encode('UTF-8'))