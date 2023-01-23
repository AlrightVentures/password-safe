# Monday night fun time - password safe 

# Import modules 
from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Define functions 
# Function creates a key - run it once to create key.key file
"""def createKey():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

createKey()
"""

# Function retrieves key data from a file
def openKey():

    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Add function allows user to add new account and password to their safe
def add():
    
    name = input("Name of your new account: ")
    password = input("Password: ")

    with open("passwords.txt", "a") as file: 
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

# View function allows users to add new account name and password to their password safe
def view():

    with open("passwords.txt", "r") as file: 
        for line in file.readlines():
            info = line.rstrip()
            user, passw = info.split("|")
            print(f"User:  {user}\nPassword: {fer.decrypt(passw.encode()).decode()}")


# TODO: Ask user for their main password to unlock the account 
# mainPasswordCheck = input("Type your main password, please.\n")


# Get key from the file and add user submitted password to it
key = openKey()
# Initialise the encryption module
fer = Fernet(key)

while True: 

    # Ask user for their master password 
    userChoice = input("Would you like to 'add' a new password or 'view' the existing ones?\nPress 'q' to quit.\n").lower()

    # Exit the software 
    if userChoice == "q": 
        break

    elif userChoice == "add":
        add()

    elif userChoice == "view":
        view()

    else:
        print("Please pick a valid option.\n")
        continue