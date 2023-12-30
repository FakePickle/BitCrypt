
from passwords import PasswordManager, generate_strong_password
from getpass import getpass


def main():
    user_auth = PasswordManager('password.json', 'key.key')

    while True:
        print("1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            email = input("Enter email: ")
            user_auth.register_user(username, password, email)

        elif choice == '2':
            username = input("Enter username: ")
            password = getpass("Enter password: ")

            if user_auth.authenticate_user(username, password):
                while True:
                    print("1. Add password\n2. Generate Password\n3. Search for a password\n4. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        website = input("Enter website: ")
                        password = getpass("Enter password: ")
                        user_auth.add_password(username, website, password)
                    
                    elif choice == '2':
                        website = input("Enter website: ")
                        length_password = input("Enter the length for password(Default value 12): ")
                        if not length_password:
                            pass
                        else:
                            user_auth.add_password(username, website, generate_strong_password(int(length_password)))

                    elif choice == '3':
                        website = input("Enter website: ")
                        user_auth.search_password(username, website)

                    elif choice == '4':
                        break

        elif choice == '3':
            break


if __name__ == "__main__":
    main()
