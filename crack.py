import pikepdf
from termcolor import colored

with open("combinations.txt", "r", encoding="latin-1") as file:
    for password in file:
        try:
            with pikepdf.open("remote.pdf", password=password.strip()) as pdf:
                print(colored("Password Found: {}".format(password), 'green'))
                break
        except:
            print(colored("Trying password: {}".format(password), 'red'))
            continue
