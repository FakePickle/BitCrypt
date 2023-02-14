import sqlite3
import getpass

conn = sqlite3.connect('UserDB.db')
cursor = conn.cursor()

class signup:
    def __init__(self,emai_id,id,pwd,confirm_pwd):
        self.mail_id = emai_id
        self.user_name = id
        self.pwd = pwd
        self.confirm_pwd = confirm_pwd
    
    def signup(self):
        cursor.execute('SELECT rowid FROM test WHERE EMAIL_ID = ?',(self.mail_id,))
        res = cursor.fetchall()
        if not(len(res)==0):
            print('A user already exists with that email id')
            user_input = input('Do you wish to sign up with different email id or login : ')
            if user_input == 'login':
                res,uname = login(input('Enter user name : '),getpass.getpass('Enter password : ')).Login()
                return res,uname
            elif user_input == 'Sign up':
                res,uname = signup(input('Enter email id : '),input('Enter user name : '),getpass.getpass('Enter password : '),getpass.getpass('Confirm your password : ')).signup()
                return res,uname
        else:
            cursor.execute('SELECT rowid FROM test WHERE USERNAME = ?',(self.user_name,))
            res = cursor.fetchall()
            if not(len(res) == 0):
                print('User already exists with that username please enter different username')
                res,uname = signup(input('Enter email id : '),input('Enter user name : '),getpass.getpass('Enter password : '),getpass.getpass('Confirm your password : ')).signup()
                return res,uname
            else:
                if self.pwd == self.confirm_pwd:
                    params = (self.mail_id,self.user_name,self.pwd,self.confirm_pwd)
                    cursor.execute('INSERT INTO test (EMAIL_ID, USERNAME, PASSWORD, CONFIRM_PASSWORD) VALUES(?,?,?,?)', params);
                    return 'You have signed up for this program',self.user_name
                else:
                    print('Passwords dont match!')
                    res,uname = signup(input('Enter email id : '),input('Enter user name : '),getpass.getpass('Enter password : '),getpass.getpass('Confirm your password : ')).signup()
                    return res,uname
        conn.commit()
        conn.close()
    
class login:
    def __init__(self,usr_name,pwd):
        self.user_name = usr_name
        self.pwd = pwd
    
    def Login(self):
        cursor.execute('SELECT rowid FROM test WHERE USERNAME = ?',(self.user_name,))
        res = cursor.fetchall()
        if not(len(res)==0):
            cursor.execute('SELECT rowid FROM test WHERE PASSWORD = ?',(self.pwd,))
            res = cursor.fetchall()
            if not(len(res)==0):
                return 'Succesfully Logged In',self.user_name
            else:
                print('Username or password is incorrect')
                res,uname = login(input('Enter user name : '),getpass.getpass('Enter password : ')).Login()
                return res,uname
        else:
            cursor.execute('SELECT rowid FROM test WHERE PASSWORD = ?',(self.pwd,))
            res = cursor.fetchall()
            if not(len(res)==0):
                cursor.execute('SELECT rowid FROM test WHERE USERNAME = ?',(self.user_name,))
                res = cursor.fetchall()
                if not(len(res)==0):
                    return 'Succesfully Logged In',self.user_name
                else:
                    print('Username or password is incorrect')
                    res,uname = login(input('Enter user name : '),getpass.getpass('Enter password : ')).Login()
                    return res,uname
            else:
                print('User does not exist')
                user_input = input('Do you wish to make new account or try to sign in again? ')
                if user_input == 'login':
                    res,uname = login(input('Enter user name : '),getpass.getpass('Enter password : ')).Login()
                    return res,uname
                elif user_input == 'sign up':
                    res,uname = signup(input('Enter email id : '),input('Enter user name : '),getpass.getpass('Enter password : '),getpass.getpass('Confirm your password : ')).signup()
                    return res,uname
        conn.close()