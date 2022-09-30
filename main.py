print(' ---Welcome--- \n\nThis is a test owned by A2d3e2\nif used (why would you?), please credit me with\nthe link "https://scratch.mit.edu/users/A2d3e2"\n')

import os

PASSWORD = os.environ['PASSWORD']
input("Press Enter")
while True:
    PASSWORDIN = input("Password: ")
    if PASSWORDIN == PASSWORD:
        break
    else:
        print("Access Denied")

os.system("clear")
print("Access Granted.")
while True:
    test = input("What test would you like to run? ")

    if test == "potato":
        print("potato")
    elif test == "add":
        a = input("Num 1: ")
        b = input("Num 2: ")
        try:
            print(f"Your number is {int(a)+int(b)}")
        except ValueError:
            print("Invalid Numbers!")
    elif test == "repeat":
        a = input("What do you want me to repeat?\n")
        print(F'"{a}"')
    elif test == "exit":
        break
    elif test == "list":
        print("potato\nadd\nrepeat\nlist\nexit")
    else:
        if not test:
            print("actually type something lol")
        else:
            print(f'"{test}" was not found.')

print("Bye")
