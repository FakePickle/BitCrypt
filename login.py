from cryptography.fernet import Fernet
import json


# Class for user authentication
class UserAuthentication:
    def __init__(self, file_path, key_file):
        self.file_path = file_path
        self.key_file = key_file
        self.key = self.load_or_generate_key()
        self.users = self.load_users_from_json()

    # Loading or generating the key if there is no key value
    def load_or_generate_key(self) -> bytes:
        try:
            with open(self.key_file, 'rb') as file:
                return file.read()
        except FileNotFoundError: # If the key file is not found, generate a new key
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
            return key # Returning the key as bytes

    # Loading the users from the JSON file
    def load_users_from_json(self) -> dict:
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file) # Returning the users as a dictionary
        except FileNotFoundError:
            return {'users': []} # Returning an empty dictionary if the file is not found

    # Saving the users to the JSON file
    def save_users_to_json(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.users, file, indent=2) # Indent=2 for pretty printing

    # Registering a new user
    def register_user(self, username: str, password: str, email: str) -> bool:

        for user in self.users['users']:
            if user['username'] == username:
                print("Username already exists. Please choose a different username.")
                return False  # Returning False if the username already exists

        fernet = Fernet(self.key)  # Setting up the Fernet object
        hashed_password = fernet.encrypt(password.encode('utf-8')).decode('utf-8')  # Encrypting the password

        new_user = {
            'username': username,
            'password': hashed_password,
            'email': email,
            'stored_passwords': [{}]
        }  # Creating a new user object

        self.users['users'].append(new_user)  # Adding the new user to the list of users
        self.save_users_to_json()  # Saving the updated list of users to the JSON file
        print(f"Welcome {username} to the program.")  # Printing a success message
        return True

    # Authenticating the user
    def authenticate_user(self, username: str, password: str) -> bool:
        for user in self.users['users']:
            if user['username'] == username:
                fernet = Fernet(self.key)
                hashed_password = user['password']
                print(fernet.decrypt(hashed_password))
                if bytes(password.encode('utf-8')) == fernet.decrypt(hashed_password):
                    return True
                else:
                    print("Incorrect password. Please try again.")
                    return False

        print("Username not found.")
        return False

