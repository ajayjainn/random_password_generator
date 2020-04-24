# Password Generator
import random
#from string import ascii_lowercase, ascii_uppercase
import string
import pyperclip
import termcolor


#alphabet = []
#for i in string.ascii_lowercase, string.ascii_uppercase:
#    alphabet += i



#numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

collection = string.punctuation + string.digits + string.ascii_uppercase + string.ascii_lowercase

def generate(length):
    password = ""
    for i in range(length):
        password += random.choice(collection)
    return password


length_input = input("What should be the length of your password?\n")
result = generate(int(length_input))
pyperclip.copy(result)
print(termcolor.colored(result, "green"))
print("Your password has been copied to clipboard :) ")



