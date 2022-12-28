import os
from msvcrt import getche

from colorama import Fore

contacts = {}


def addContact():
    f = open("contact.txt", 'a')
    print(Fore.YELLOW + "enter the name : ", end="")
    name = input()
    print(Fore.YELLOW + "enter the phone number : ", end="")
    phoneNumber = input()
    f.write(name)
    f.write(" : ")
    f.write(phoneNumber)
    f.write("\n")
    print(Fore.LIGHTGREEN_EX + "contact added successfully")
    print(Fore.LIGHTGREEN_EX + "press any key to exit from here")
    c = getche()


def showContact():
    f = open("contact.txt", 'r')
    contact = []
    for line in f:
        contact.append(line)
    for i in contact:
        temp = i.split(" : ")
        print(Fore.BLUE + temp[0], end="")
        print(" : ", end="")
        print(Fore.LIGHTMAGENTA_EX + temp[1])
    print(Fore.LIGHTGREEN_EX + "press any key to exit from here")
    c = getche()


while True:
    os.system("cls")
    print(Fore.LIGHTWHITE_EX + "             welcome            ")
    print(Fore.LIGHTWHITE_EX + "          1.add contact         ")
    print(Fore.LIGHTWHITE_EX + "         2.show contacts        ")
    print(Fore.LIGHTWHITE_EX + "             3.exit             ")
    ch = input()
    if ch == '1':
        addContact()
    elif ch == '2':
        showContact()
    elif ch == '3':
        exit()
    else:
        print(Fore.RED + "invalid input")
        c = getche()