import os
import platform


def files():
    exists = os.path.isfile("login.txt")
    if not exists:
        username = input("username: ")
        password = input("password: ")

        f = open("login.txt", "w")
        f.write(username + ":" + password)
        f.close()

files()



