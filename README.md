# Bitwarden Password Manager

Bitwarden Password Manager is a secure and lightweight command-line password manager written in Python. It allows users to securely store, generate and manage their passwords.

## Features

- **User-Friendly**: Simple and intuitive command-line interface for easy navigation.
- **Secure Authentication**: Protect your passwords with robust user authentication.
- **Password Generation**: Generate strong and unique passwords effortlessly.
- **Efficient Searching**: Quickly find and retrieve passwords when you need them.

<img width="400" height="300" alt="bitwarden-1" src="https://github.com/FakePickle/Bitwarden_from_Wish/assets/122410275/ea305564-15ae-4ddf-85da-5a2a6030f095">
<img width="400" height="300" alt="bitwarden-2" src="https://github.com/FakePickle/Bitwarden_from_Wish/assets/122410275/f446d54f-ec28-464c-b810-a8caa338ba3d">

## Prerequisites

- Python 3.x
- Python Libraries
    - `cryptography`: Used for encryption and decryption of passwords.
    - `colorama`: Adds color to the terminal for a better user experience.
    - `getpass4`: Enhances the password input functionality.
    - `sockets`: Handles communication between the server and client.
    - `bcrypt`: Ensures secure password hashing.

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/FakePickle/Bitwarden.git
    ```

2. Change the directory to bitwarden:

    ```bash
    cd bitwarden
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python main.py
    ```

## Usage

Follow the on-screen instructions to navigate through the application. You can sign up, log in, add passwords, generate strong passwords, and search for existing passwords.

## File Structure

Bitwarden

    ├── src
    |    ├── main.py
    |    ├── login.py
    |    ├── file_transfer.py
    |    ├── password.py
    ├── data 
    |    ├── password.json
    |    ├── key.key
    ├── requirements.txt
    ├── LICENSE.md
    ├── README.md

- **`src`**: Contains the main source code files.
    - `main.py`: The main script to run the Bitwarden Password Manager.
    - `login.py`: Handles user authentication and registration.
    - `file_transfer.py`: Provides functionality for transferring files between the server and client.
    - `password.py`: Manages password-related functionality, including password generation.

- **`data`**: Stores data files used by the application.
    - `password.json`: JSON file for storing user data.
    - `key.key`: Key file for encryption.

- **`requirements.txt`**: Lists the required dependencies for the project.

- **`LICENSE.md`**: The license file for the project.

- **`README.md`**: The main README file with information about the project.


## Contributing

Welcome to contribute to Bitwarden Password Manager! Feel free to fork the repository and suggest any improvements. To contribute, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push the changes to your fork.
5.  Submit a pull request.

Thank you for your contributions!

## License

This project is licensed under the [MIT License](LICENSE.md).

## Author

[Harsh Mistry](https://github.com/FakePickle)
\
[Vikranth Udandarao](https://github.com/Vikranth3140)