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

user_input = input("Enter any word : ")
user_input = bytes(user_input, 'utf-8')
x = Encrypt(user_input)
a = x.encrypt()
print(a)
print(x.decrypt(a))