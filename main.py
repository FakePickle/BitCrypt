from file_transfer import file_Transfer
import time
from passwords import main,key
from encrypt_decrypt import encrypt_decrypt
import getpass
from login import login,signup

class magic:
    def __init__(self,user_name_input,website):
        self.usr_name = user_name_input
        self.web = website

    def write_key():
        try:
            with open('key.key','rb') as inline:
                if len(inline.read().splitlines())==0:
                    key()
        except:
            key()

    def search_passwords(self):
        inline = open('passwords.txt')
        inline = eval(inline.read())
        for keys,values in inline.items():
            for k,v in values.items():
                if k == self.web:
                    temp_list = v
        email = temp_list[0]
        pwd = temp_list[1]
        with open('key.key','rb') as inline:
            data = inline.read().splitlines()
        key1 = data[0]
        key2 = data[1]
        decryption = encrypt_decrypt(key1,key2)
        mail = decryption.decrypt_file(email)
        password = decryption.decrypt_file(pwd)
        return str(mail),str(password)

class File_transfer:
    def __init__(self):
        self.file = file_Transfer()
    
    def main_time(self):
        run = True
        while run:
            role = 'client' if time.time() % 30 < 15 else 'host'
            if role == 'host':
                self.file.server_usr()
                print('HOST')
            elif role == 'client':
                self.file.client_usr()
                user_input_cl = input()
                print('CLIENT')
                if user_input_cl == 'recv': run = False
            time.sleep(15)
        if user_input_cl == 'recv':
            sch = magic(input('Enter user name : '),input('Enter website : '))
            sch.write_key()
            sch.search_passwords()
        if input() == 'kill':
            run = False
        else:
            run = True
        if run:
            File_transfer().main_time()
        else:
            print('Program killed !')

if __name__ == '__main__':
    user_input_ch = input('Do you want to login or signup : ')
    if user_input_ch == 'login':
        user_login = login(input('Enter user name : '),getpass.getpass('Enter your password : ','*'))
        res,user_name = user_login.Login()
    elif user_input_ch == 'signup':
        user_signup = signup(input('Enter your email id : '),input('Enter your username : '),getpass.getpass('Enter your password : ','*'),getpass.getpass('Confirm your password','*'))
        res,user_name = user_signup.signup()
    if res == 'Succesfully Logged In' or res == 'You have signed up for this program':
        while True:
            user_input = input('Do you want to search a password or add a password? ')
            if user_input == 'add password':
                main(user_name)
            elif user_input == 'search password':
                print(magic(input('Enter user name : '),input('Enter website : ')).search_passwords())
            else:
                print('Invalid Input')
                break