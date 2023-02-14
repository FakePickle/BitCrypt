from cryptography.fernet import Fernet

class encrypt_decrypt:
    def __init__(self):
        self.key1 = Fernet.generate_key()
        self.key2 = Fernet.generate_key()
        self.fernet1 = Fernet(self.key1)
        self.fernet2 = Fernet(self.key2)
    
    def key_write(self):
        f = open('key.key','wb')
        f.write(self.key1)
        f.write(self.key2)
        f.close()

    def encrypt_file(self,usr_input):
        encryption1 = self.fernet1.encrypt(bytes(usr_input,'utf-8'))
        encryption2 = self.fernet2.encrypt(encryption1)
        return encryption2
    
    def decrypt_file(self,encryption):
        decryption1 = self.fernet2.decrypt(encryption)
        decryption2 = self.fernet1.decrypt(decryption1)
        return decryption2