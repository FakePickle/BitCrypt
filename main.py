from file_transfer import file_Transfer
import time
from passwords import main,key
from encrypt_decrypt import encrypt_decrypt

class magic:
    def __init__(self,user_name_input,website):
        self.usr_name = user_name_input
        self.web = website
    
    def main(self):
        inline = open('passwords.txt')
        inline = eval(inline.read())
        for values in inline[self.usr_name]:
            for v in values[self.web]:
                temp_list = v
        email = temp_list[0]
        pwd = temp_list[1]
        keys = open('key.key')
        