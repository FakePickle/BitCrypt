import socket

bind_ip = '192.168.60.51'
bind_port = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((bind_ip, bind_port))
host = socket.gethostname()
print(host)
ip = socket.gethostbyname(host)

client.send(str.encode(ip))
client.close()