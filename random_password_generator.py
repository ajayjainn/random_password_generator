# Password Generator
import random
import string
import pyperclip
import termcolor

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



