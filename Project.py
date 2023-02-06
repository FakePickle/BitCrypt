from cryptography.fernet import Fernet
import curses
import os
import time
import pickle
import sqlite3
import socket


#----------------------------------------------------------------BASE ENCRYPTION AND DECRYPTION-------------------------------------------------------------------------

class Encrypt:
    def __init__(self,user_input):
        self.key1 = Fernet.generate_key()
        self.key2 = Fernet.generate_key()
        self.crypto1 = Fernet(self.key1)
        self.crypto2 = Fernet(self.key2)
        self.word = user_input
    
    #Encrypting
    def encrypt(self):
        first_encrypt = self.crypto1.encrypt(self.word)#first encryption
        second_encrypt = self.crypto2.encrypt(first_encrypt)#second encryption
        return second_encrypt
    
    #Decrypting
    def decrypt(self,encrypted_key):
        first_decrypt = self.crypto2.decrypt(encrypted_key)#first decryption
        second_decrypt = self.crypto1.decrypt(first_decrypt)#second decryption
        return second_decrypt

class Connect:
    def __init__(self):
        self.ip_addr_list = ['192.168.60.68','192.168.61.96']
        self.ip_bind = '192.168.60.51'
        self.port_bind = '9999'
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    def connect(self):
        ip_bind = random.choice(self.ip_bind)
        self.server.bind((ip_bind, self.port_bind))
        self.server.listen(15)
        conn, addr = self.server.accept()
        

user_input = input("Enter any word : ")
user_input = bytes(user_input, 'utf-8')
x = Encrypt(user_input)
a = x.encrypt()
print(a)
print(x.decrypt(a))