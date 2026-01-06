import random

def random_number():
    print("Random Number:", random.randint(1, 100))

def random_password():
    characters = "qwertyuiop7410852@#!$"
    password = ""
    for i in range(6):
        password = password + random.choice(characters)
    print("Password:", password)