import socket
import datetime
print(datetime.datetime.now())
bin_ip = '192.168.60.51'
bin_port = 8080
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((bin_ip,bin_port))
server.listen(30)
conn,addr = server.accept()
print(datetime.datetime.now())
print(addr[0])