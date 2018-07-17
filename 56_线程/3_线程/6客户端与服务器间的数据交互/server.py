import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.56.1',8085))

server.listen(5)
print("服务器启动成功...")

def run(ck):
    data = clientSocket.recv(1024)
    print("客户端说:" + data.decode("utf-8"))
    # sendData = input("返回给客户端的数据:")
    clientSocket.send("turo is a good man".encode("utf-8"))

while True:
    clientSocket, clientAddress = server.accept()
    #print("%s -- %s 连接成功" % (str(clientSocket), clientAddress))
    t = threading.Thread(target=run, args=(clientSocket,))
    t.start()

    '''
    data = clientSocket.recv(1024)
    print("客户端说:" + data.decode("utf-8"))
    sendData = input("返回给客户端的数据:")
    clientSocket.send(sendData.encode("utf-8"))
    '''

'''
实际上:
while True:
    #等待客户端连接
    clientSocket, clientAddress = server.accept()
    #启动一个线程, 将当前连接的clientSocket交给线程
'''
