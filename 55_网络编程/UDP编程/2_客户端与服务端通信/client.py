import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input("请输入数据:")
    client.sendto(data.encode("utf-8"), ("169.254.43.120", 8095))
    info = client.recv(1024).decode("utf-8")
    print("服务器说:", info)
