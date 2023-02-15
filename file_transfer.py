import socket

class file_Transfer:
    def __init__(self):
        self.bind_ip = '192.168.60.51'
        self.bind_port = 9999
        self.size = 4096
        self.format = 'utf-8'
    
    def server_usr(self):
        host_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_sock.bind((self.bind_ip, self.bind_port))
        host_sock.listen()
        print('Waiting for a connection...')
        connection, client_address = host_sock.accept()
        try:
            print('Accepted connection from:', client_address)
            with open('passwords.txt', 'rb') as f, open('key.key','rb') as inline:
                connection.sendall(f.read())
                connection.sendall(inline.read())
                print('Files Sent')
        finally:
            connection.close()
        host_sock.close()
    
    def client_usr(self):
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((self.bind_ip,self.bind_port))
        with open('passwords.txt','wb') as f, open('key.key','wb') as outline:
            f.write(client.recv(self.format))
            outline.write(client.recv(self.format))
            print('Files received')
        client.close()