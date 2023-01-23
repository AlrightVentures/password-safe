# Monday night fun time - password safe 

# Import modules 
from cryptography.fernet import Fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Define functions 
# Function creates a key - run it once to create key.key file that will store your key
"""def createKey():
    key = Fernet.generate_key()

    with open("key.key", "wb") as key_file:
        key_file.write(key)

createKey()
"""

# Function retrieves key data from a file
def openKey():

    # Open the key,key file in the read bytes mode
    file = open("key.key", "rb")
    # Read data from the file
    key = file.read()
    # Close the file to avoid problems
    file.close()
    # Return key to be used 
    return key


# Add function allows user to add new account and password to their safe
def add():
    
    # User to add name of the account and password they want to store in the safe
    name = input("Name of your new account: ")
    password = input("Password: ")

    # Add new info to the end of the file storing passwords
    with open("passwords.txt", "a") as file: 
        file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

# View function allows users to add new account name and password to their password safe
def view():

    # Open the file storing passwords
    with open("passwords.txt", "r") as file: 
        # Read the file line by line 
        for line in file.readlines():
            # Strip the \n character from the line
            info = line.rstrip()
            # Store account, password info in separate variables
            account, passw = info.split("|")
            print(f"Account:  {account}\nPassword: {fer.decrypt(passw.encode()).decode()}")


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
    # Run add function
    elif userChoice == "add":
        add()
    # Run view function
    elif userChoice == "view":
        view()
    # User submitted invalid option. Ask user to provide a valid option. Goes back to the start of loop.
    else:
        print("Please pick a valid option.\n")
        continue


# Made with love.
# Check out Harry Mack on YouTube. 
# Have a great day.