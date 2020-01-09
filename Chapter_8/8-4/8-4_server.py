import socket
import threading

client_list = []

# 第一个参数指定网络类型：
# AF_INET，代表IPv4网络；AF_INET6，代表IPv6网络；AF_UNIX，代表UNIX的网络
# 第二个参数指定Socket的类型，包括SOCK_STREAM（TCP协议），NI_DGRAM（UDP协议）
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

# 有了socket之后，接下来还需要绑定到本机指定IP和端口、监听来自客户端的连接、接收来自客户端的连接
# 创->绑->监->接
# 绑定到指定的IP和端口
s.bind(("192.168.1.55", 30000))
# 监听
s.listen()


def server_target(server_socket):
    # 一旦建立连接之后，server与client虚拟链路建立成功
    while True:
        content = server_socket.recv(2048).decode('UTF-8')
        if content is not None:
            # 读取到数据之后，将数据打印出来
            print(content)
            # 将数据送回给每个客户端
            for cl in client_list:
                cl.send(content.encode('UTF-8'))


while True:
    # 接收来自客户端的连接
    # 该方法返回两个参数，c代表与客户端socket对应的、通信用的socket、addr代表客户端的地址
    c, addr = s.accept()
    print(addr)

    # 将所有客户端对应的socket保存到列表中
    client_list.append(c)
    # 为客户端对应的socket启动对应的线程
    threading.Thread(target=server_target, args=(c,)).start()