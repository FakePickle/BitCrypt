# Bitwarden_from_Wish

The purpose of this project is to make the passwords that we store more hard to access or crack by
a hacker.
Our project solely depends on 2 laptops(servers) atleast running so we wouldnt have an error while running the code.
It works in way that the password file and the keys(used to decrypt the passwords) being sent to the laptop of different user using sockets(transferring files over https) and deleting the existing file in the host laptop so it will have no footprint at a time interval of every 15 seconds.
The passwords are stored in byte format. We are also using a database so that we will be able to access that specific user's passwords and those passwords will be stored under that user only.
The database we are using is sqlite3.
We have a total of 5 files. All files are functioning according to the names indicating it like encrypt_decrypt.py is used for encrypting the data and also decrypting the data and login.py file is where entire login/signup process takes place, etc..
passwords.txt is a file where all the passwords are stored and key.key is a file where the keys have been stored accordingly.
We have also given users option to either generate a strong enough password or input their desired password in the password manager and given the user privacy while inputting the password for that we have used a module named getpass which hides the text whlie taking input.
Unfortunately, due to the lack of time we were unable to create a good gui using tkinter/curses hence everything would be done on terminal only.
Thanks.
Project Done By:- Harsh Priteshkumar Mistry(2022200), Vikranth Udandarao(2022570), Armaan Singh(2022096)