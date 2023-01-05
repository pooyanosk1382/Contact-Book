import os
from msvcrt import getche

from colorama import Fore

contacts = {}


def addContact():
    f = open("contact.txt", 'r')
    print(Fore.YELLOW + "enter the name : ", end="")
    name = input()
    print(Fore.YELLOW + "enter the phone number : ", end="")
    phoneNumber = input()
    tempName = []
    tempNum = []
    for i in f:
        temp1 = i.split(" : ")
        if len(temp1) <= 1:
            continue
        tempName.append(temp1[0])
        tempNum.append(temp1[1])
    for i in range(len(tempName)):
        print(tempNum[i], phoneNumber)
        if tempName[i] == name:
            print(Fore.RED + "This name is already taken")
            print("press any key to return")
            c = getche()
            return
        elif tempNum[i].__contains__(phoneNumber):
            print(Fore.RED + "This number is already taken")
            print("press any key to return")
            c = getche()
            return
    f.close()
    f = open("contact.txt", 'a')
    f.write(name)
    f.write(" : ")
    f.write(phoneNumber)
    f.write("\n")
    f.close()
    f = open("contact.txt", 'r')
    tempName = []
    tempNum = []
    for i in f:
        temp1 = i.split(" : ")
        if len(temp1) <= 1:
            continue
        tempName.append(temp1[0])
        tempNum.append(temp1[1])
    num = [x for _, x in sorted(zip(tempName, tempNum))]
    tempName.sort()
    f.close()
    f = open("contact.txt", 'w')
    for i in range(len(tempName)):
        f.write(tempName[i])
        f.write(" : ")
        f.write(num[i])
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
        if len(temp) <= 1:
            continue
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