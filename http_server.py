"""
http 协议服务器代码，传输层只能是ＴＣＰ协议
"""
from socket import *
ADDR = ("127.0.0.1",10000)
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(10)
    while True:
    # 等待客户端连接
        connfd,addr = sockfd.accept()
        info = request(connfd)
        print(info)
        if info=="/":
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            with open("http_ex.html","r") as f:
                response += f.read()
            connfd.send(response.encode())
        else:
            response = "HTTP/1.1 404 NOT Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += "sorry.."
            connfd.send(response.encode())

def request(connfd):
    data = connfd.recv(1024*4)
    if not data:
        return
    request_line=data.decode().split("\n")[0]
    info = request_line.split(" ")[1]

    return info

if __name__=="__main__":
    main()