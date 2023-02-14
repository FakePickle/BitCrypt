from encrypt_decrypt import encrypt_decrypt,keys
import getpass
from login import login,signup
import secrets
import string

def key():
    key = keys()
    key.key_write()

def generate_password(length = 16):
    alphabot = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabot) for i in range(length))

def main():
    with open('key.key','rb') as inline:
        keys = inline.read().splitlines()
    encryption = encrypt_decrypt(keys[0],keys[1])
    user_input_ch = input('Do you want to login or signup : ')
    if user_input_ch == 'login':
        user_login = login(input('Enter user name : '),getpass.getpass('Enter your password : ','*'))
        res,user_name = user_login.Login()
    elif user_input_ch == 'signup':
        user_signup = signup(input('Enter your email id : '),input('Enter your username : '),getpass.getpass('Enter your password : ','*'),getpass.getpass('Confirm your password','*'))
        res,user_name = user_signup.signup()
    if res == 'Succesfully Logged In' or res == 'You have signed up for this program':
        user_input_pass = input('Do you want to generate a password : ')
        if user_input_pass.lower() == 'yes':
            user_input_mail = input('Enter mail id : ')
            user_input_website = input('Enter the password storing is for which website : ')
            user_input_password = generate_password()
        elif user_input_pass.lower() == 'no':
            user_input_mail = input('Enter mail id : ')
            user_input_website = input('Enter the password storing is for which website : ')
            user_input_password = getpass.getpass('Enter your password : ')
    try:
        with open('passwords.txt') as inline:
            pass_dict = eval(inline.read())
            if pass_dict == '':
                pass_dict = {}
    except:
        pass_dict = {}
    if pass_dict == {}:
        pass_dict[user_name] = {
            user_input_website : [encryption.encrypt_file(user_input_mail),encryption.encrypt_file(user_input_password)]
        }
    else:
        temp_dict = {}
        if user_name in pass_dict.keys():
            temp_dict[user_input_website] = [encryption.encrypt_file(user_input_mail),encryption.encrypt_file(user_input_password)]
        else:
            pass_dict[user_name] = {
            user_input_website : [encryption.encrypt_file(user_input_mail),encryption.encrypt_file(user_input_password)]
        }
        if temp_dict == {}:
            pass
        else:
            for k,v in pass_dict.items():
                if k == user_name:
                    v = {**v,**temp_dict}
                    pass_dict[k] = v
                    break
    with open('passwords.txt','w') as outline:
        outline.write(str(pass_dict))