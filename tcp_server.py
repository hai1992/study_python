import socket

"""
重点代码
ｔｃｐ套接字服务器端流程
1创建服务器端套接字
sockfd = socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0)
family：网络地址，默认ｉｐｖ４，用AF_INET表示
type:套接字类型，默认SOCK_STREAM（流式）,SOCK_DGRAM(数据报式)
proto　通常为0　作用选择子协议
2绑定地址blid
sockfd.blid(addr)
地址格式addr　（“ip”，端口号）
本地地址："localhost","127.0.0.1"
网络地址： ifconfig 获取网络地址
自动获取地址："0.0.0.0"
3设置监听
sockfd.listen(n)
将套接字设置为监听套接字，确定监听队列大小ｎ
4等待处理客户端连接请求
connfd, addr= sockfd.accept()
功能：阻塞等待处理客户端请求
connfd 新的客户端套接字
addr 　连接的客户端地址
５消息收发
收消息
data = connfd.recv(buffersize)
功能：接受客户端消息
buffersize　接受的信息大小
返回值：接受的内容
发消息
n = connfd.send(data)
功能：发送消息
data　发送内容　ｂｙｔｅｓ格式
n 发送的字节数
６　关闭套接字
sockfd.close()

＃测试　在终端输入telnet ip 端口号　　建立连接
"""
# 创建服务器端套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 设置套接口属性，端口可立即被重置
sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

# 绑定地址
sockfd.bind(("0.0.0.0",10000))
# 设置监听
sockfd.listen(5)
# 等待连接
# print("等待连接．．．．")
# connfd,addr = sockfd.accept()
# print("连接成功",addr)
# 收发消息
# data = connfd.recv(1024)
# print("收到：",data.decode())
# n = connfd.send("００".encode())
# print("发送字节",n)

# 增加功能,循环接受消息，想断开就断开
# while True:
#     data = connfd.recv(1024)
#     if data.decode() == "##":
#         break
#     print("收到：", data.decode())
#     n = connfd.send("００".encode())
#     print("发送字节", n)
# 关闭套接字
# connfd.close()
# sockfd.close()
# 进阶版，一个客户端突然断开链接　服务器不断开继续等待新的客户端连接
while True:
    print("等待连接．．．．")
    try:
        # 如果一直没有新的客户端连接，直接关闭服务器端会出KeyboardInterrupt异常
        connfd,addr = sockfd.accept()
        print("连接成功",addr)
    except KeyboardInterrupt as k:
        print(k)
        break
    except Exception as e:
        print(e)
        continue
    # 收发消息
    # data = connfd.recv()
    # print("收到：",data.decode())
    # n = connfd.send("００".encode())
    # print("发送字节",n)

    # 增加功能,循环接受消息，想断开就断开
    while True:
        data = connfd.recv(3072)
        #如果客户端直接断开，recv解除堵塞，直接返回空
        if not data:
            break
        # if data == b"##":
        #     break
        print("收到：", data.decode())
        n = connfd.send("００－－".encode())
        print("发送字节", n)
    connfd.close()
sockfd.close()


#

