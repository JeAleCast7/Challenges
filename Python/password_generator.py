import string
import random

def password_generator():

    length = int(input("Enter the length of the password: "))
    if length < 8 or length > 16:
            print("Password must be between 8 and 16 characters")
            return

    upper = input("Do you want upper letters? yes/no: ").lower()
    numbers = input("Do you want numbers? yes/no: ").lower()
    symbols = input("Do you want symbols? yes/no: ").lower()

    characters = string.ascii_lowercase

    if upper == "yes":
        characters += string.ascii_uppercase

    if numbers == "yes":
        characters += string.digits

    if symbols == "yes":
        characters += string.punctuation

    password = ""
    for l in range(length):
        password += random.choice(characters)

    print(password)

password_generator()

#import string — te da los alfabetos listos:
#pythonstring.ascii_lowercase  # → "abcdefghijklmnopqrstuvwxyz"
#string.ascii_uppercase  # → "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#string.digits           # → "0123456789"
#string.punctuation      # → "!@#$%^&*()..." etc