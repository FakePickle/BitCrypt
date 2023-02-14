from cryptography.fernet import Fernet

class keys:
    def __init__(self):
        self.key1 = Fernet.generate_key()
        self.key2 = Fernet.generate_key()

    def key_write(self):
        f = open('key.key','wb')
        f.write(self.key1)
        f.write('\n')
        f.write(self.key2)
        f.close()

class encrypt_decrypt:
    def __init__(self,key1,key2):
        self.key1 = key1
        self.key2 = key2
        self.fernet1 = Fernet(self.key1)
        self.fernet2 = Fernet(self.key2)

    def encrypt_file(self,usr_input):
        encryption1 = self.fernet1.encrypt(bytes(usr_input,'utf-8'))
        encryption2 = self.fernet2.encrypt(encryption1)
        return encryption2
    
    def decrypt_file(self,encryption):
        decryption1 = self.fernet2.decrypt(encryption)
        decryption2 = self.fernet1.decrypt(decryption1)
        return decryption2