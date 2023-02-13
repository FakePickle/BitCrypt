import sqlite3

conn = sqlite3.connect('UserDB.db')
cursor = conn.cursor()

class login:
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
                login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).Login()
            elif user_input == 'Sign up':
                login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).signup()
        else:
            cursor.execute('SELECT rowid FROM test WHERE USERNAME = ?',(self.user_name,))
            res = cursor.fetchall()
            if not(len(res) == 0):
                print('User already exists with that username please enter different username')
                login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).signup()
            else:
                if self.pwd == self.confirm_pwd:
                    params = (self.mail_id,self.user_name,self.pwd,self.confirm_pwd)
                    cursor.execute('INSERT INTO test (EMAIL_ID, USERNAME, PASSWORD, CONFIRM_PASSWORD) VALUES(?,?,?,?)', params);
                    print('You have Succesfully Signed up for this program!!')
                else:
                    print('Passwords dont match!')
                    login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).signup()
        conn.commit()
        conn.close()
    
    def Login(self):
        cursor.execute('SELECT rowid FROM test WHERE USERNAME = ?',(self.user_name,))
        res = cursor.fetchall()
        if not(len(res)==0):
            cursor.execute('SELECT rowid FROM test WHERE PASSWORD = ?',(self.pwd,))
            res = cursor.fetchall()
            if not(len(res)==0):
                print('Succesfully Logged In')
                conn.close()
            else:
                print('Username or password is incorrect')
                login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).Login()
        else:
            cursor.execute('SELECT rowid FROM test WHERE PASSWORD = ?',(self.pwd,))
            res = cursor.fetchall()
            if not(len(res)==0):
                cursor.execute('SELECT rowid FROM test WHERE USERNAME = ?',(self.user_name,))
                res = cursor.fetchall()
                if not(len(res)==0):
                    print('Succesfully Logged In')
                    conn.close()
                else:
                    print('Username or password is incorrect')
                    login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).Login()
            else:
                print('User does not exist')
                user_input = input('Do you wish to make new account or try to sign in again? ')
                if user_input == 'login':
                    login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).Login()
                elif user_input == 'sign up':
                    login(input('Enter email id : '),input('Enter user name : '),input('Enter password : '),input('Confirm your password : ')).signup()