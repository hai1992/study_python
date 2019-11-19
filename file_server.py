"""
网络传输文件服务器端代码
"""
import socket

socked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("0.0.0.0", 12345)
socked.bind(address)
socked.listen(5)
while True:

    try:
        print("等待连接．．．")
        # 如果一直没有新的客户端连接，直接关闭服务器端会出KeyboardInterrupt异常
        connfd, addr = socked.accept()
        print("连接成功", addr)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        continue
    file = open("result_file","wb+")
    while True:
        data = connfd.recv(1024)
        if not data:
            file.close()
            break
        file.write(data)
        file.flush()
        n = connfd.send("收到！".encode())
    connfd.close()
socked.close()

