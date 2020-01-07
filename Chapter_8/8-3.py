import socket

#第一个参数指定网络类型：
#AF_INET，代表IPv4网络；AF_INET6，代表IPv6网络；AF_UNIX，代表UNIX的网络
#第二个参数指定Socket的类型，包括SOCK_STREAM（TCP协议），NI_DGRAM（UDP协议）
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

#有了socket之后，接下来还需要绑定到本机指定IP和端口、监听来自客户端的连接、接收来自客户端的连接
#创->绑->监->接
#绑定到指定的IP和端口
s.bind(("192.168.1.55",30000))
#监听
s.listen()
while True:
    #接收来自客户端的连接
    #该方法返回两个参数，c代表与客户端socket对应的、通信用的socket、addr代表客户端的地址
    c,addr=s.accept()
    print(addr)
    #后面即可通过c与客户端进行通信
    #socket有send,recv两个方法用于发送和接收数据
    c.send('我是服务端！'.encode('UTF-8'))
    #关闭资源
    c.close()