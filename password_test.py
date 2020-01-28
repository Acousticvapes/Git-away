import re

def pass_test():
    value = 0
    password = input("Enter your password: ")
    if re.search('[a-z]', password):
        value = value + 1 #adds 1 to value if it includes lower cases letters
    if re.search('[A-Z]', password):
        value = value + 1
    if re.search('[0-9]', password):
        value = value + 1
    if re.search('[!@#$%^&*()_+-=;'",./<>?`~`"']', password):
        value = value + 1
    if len(password) < 8:
        print("Password must be 8 character or more")
    if value == 4:
        print("Password is great")
    if value == 3:
        print("Password is okay")
    if value == 2:
        print("Password is weak")
    if value == 1:
        print("Dont even try this one")
    return 0
pass_test()
