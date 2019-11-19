"""
网络文件传输客户端代码
"""
import socket

sockfd = socket.socket()
address = ("0.0.0.0",12345)
sockfd.connect(address)
file = open("../RE/exc.txt","rb")
while True:
    data = file.read(1024)
    if not data:
        break
    sockfd.send(data)
    msg = sockfd.recv(1024)
    print("服务器信息：",msg.decode())

file.close()
sockfd.close()
