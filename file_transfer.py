import socket

class file_Transfer:
    def __init__(self):
        self.bind_ip = socket.gethostbyname(socket.gethostname())
        self.bind_port = 9999
        self.size = 2048
        self.format = 'utf-8'
    
    def server_usr(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((self.bind_ip,self.bind_port))
        server.listen()
        conn,addr = server.accept()
        inline = open('file1.txt')
        data = inline.read()
        conn.send(data.encode(self.format))
        inline.close()
        inline = open('key.key')
        data = inline.read()
        conn.send(data.encode(self.format))
        server.close()
    
    def client_usr(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((self.bind_ip,self.bind_port))
        data = client.recv(self.size).decode(self.format)
        outline = open('test2.txt','w')
        outline.write(data)
        outline.close()
        client.close()