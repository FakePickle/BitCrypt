from cryptography.fernet import Fernet
from login import UserAuthentication
import string
import secrets


def generate_strong_password(length: int = 12) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    secure_password = ''.join(secrets.choice(characters) for _ in range(length))
    return secure_password


class PasswordManager(UserAuthentication):
    def __init__(self, file_path, key_file):
        super().__init__(file_path, key_file)
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        try:
            with open(self.key_file, 'rb') as file:
                return file.read()
        except FileNotFoundError:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
            return key

    def add_password(self, username: str, website: str, password: str) -> bool:
        for user in self.users['users']:
            if user['username'] == username:
                fernet = Fernet(self.key)
                encrypted_password = fernet.encrypt(password.encode('utf-8')).decode('utf-8')
                user['stored_passwords'][0][website] = encrypted_password
                self.save_users_to_json()
                print(f"Password for {website} added successfully.")
                return True

        print("Username not found.")
        return False

    def search_password(self, username: str, website: str) -> None:
        for user in self.users['users']:
            if user['username'] == username:
                stored_passwords = user['stored_passwords'][0]
                if website in stored_passwords:
                    fernet = Fernet(self.key)
                    decrypted_password = fernet.decrypt(stored_passwords[website].encode('utf-8')).decode('utf-8')
                    print(f"Password for {website}: {decrypted_password}")
                    return
                else:
                    print(f"No password found for {website}")
                    return

        print("Username not found.")
