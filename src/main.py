from passwords import PasswordManager, generate_strong_password
from getpass4 import getpass
import colorama
from colorama import Fore, Style
import os


# Clearing the screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Displaying the intro
def display_intro():
    clear_screen()
    colorama.init(autoreset=True)  # Initializing colorama

    print(Fore.CYAN + r'''
__________.__  __   _________                        __   
\______   \__|/  |_ \_   ___ \_______ ___.__._______/  |_ 
 |    |  _/  \   __\/    \  \/\_  __ <   |  |\____ \   __\
 |    |   \  ||  |  \     \____|  | \/\___  ||  |_> >  |  
 |______  /__||__|   \______  /|__|   / ____||   __/|__|  
        \/                  \/        \/     |__|         
    ''' + Style.RESET_ALL)  # Printing the logo

    print(Fore.YELLOW + "Welcome to BitCrypt Password Manager!\n")  # Printing the welcome message


# Main function
def main():
    display_intro()
    user_auth = PasswordManager('../data/password.json', '../data/key.key')  # Creating a new PasswordManager object

    while True:
        print("-----------------------------------------------------")
        print("1. Signup\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("-----------------------------------------------------")
            username = input("Enter username: ")
            email = input("Enter email: ")
            password = getpass("Enter password: ")
            print("-----------------------------------------------------")
            user_auth.register_user(username, password, email)

        elif choice == '2':
            print("-----------------------------------------------------")
            username = input("Enter username: ")
            password = getpass("Enter password: ", "*")
            print("-----------------------------------------------------")

            if user_auth.authenticate_user(username, password):
                clear_screen()
                print(f'\033[1mWelcome {username}.\0330')
                while True:
                    print("-----------------------------------------------------")
                    print("1. Add password\n2. Search for a password\n3. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':

                        while True:
                            print("-----------------------------------------------------")
                            print("1. Add password manually\n2. Generate a strong password\n3. Go back")
                            choice = input("Enter your choice: ")

                            if choice == '1':  # Adding password manually
                                print("-----------------------------------------------------")
                                website = input("Enter website: ")
                                password = getpass("Enter password: ", "*")
                                print("-----------------------------------------------------")
                                user_auth.add_password(username, website, password)
                                break

                            elif choice == '2':  # Generating a strong password
                                print("-----------------------------------------------------")
                                website = input("Enter website: ")
                                length_password = input("Enter the length for password(Default value 12): ")
                                print("-----------------------------------------------------")
                                if not length_password:
                                    user_auth.add_password(username, website, generate_strong_password())
                                else:
                                    user_auth.add_password(username, website,
                                                           generate_strong_password(int(length_password)))
                                break

                    elif choice == '2':  # Searching for a password
                        print("-----------------------------------------------------")
                        website = input("Enter website: ")
                        print("-----------------------------------------------------")
                        user_auth.search_password(username, website)

                    elif choice == '3':  # Logging out
                        print(f"Logged out of {username}.")
                        clear_screen()
                        break

        elif choice == '3':  # Exiting the program
            print("Thank you for using BitCrypt. Hope you have a wonderful day ahead")
            clear_screen()
            break


if __name__ == "__main__":
    main()
