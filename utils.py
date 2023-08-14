import random

def get_new_pass():
    elements = "0123456789!@#$%^&*()qwertyuiopasdfghjkl;zxcvbnm"
    password = ""
    pass_length = 8

    for i in range(pass_length):
        password += random.choice(elements)
    return password