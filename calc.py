import os
import time

def title():
    purple = '\033[95m'
    reset = '\033[0m'
    text = '''      _____      _            _       _             
     / ____|    | |          | |     | |            
    | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | |___| (_| | | (__| |_| | | (_| | || (_) | |   
     \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   '''
    print(purple + text + reset)
    print("            Version 1.1   by LouisVDE")

def ft_ope(nbr_1, nbr_2):
    nbr_3 = 0
    ope = input("Enter an operator: ")
    if ope == "exit":
        return None
    if ope not in ["+", "-", "*", "/", "AC", "ac"]:
        print("Error, invalid operator")
        return
    if ope == "+":
        nbr_3 = float(nbr_1) + float(nbr_2)
        print(nbr_3)
    elif ope == "-":
        nbr_3 = float(nbr_1) - float(nbr_2)
        print(nbr_3)
    elif ope == "*":
        nbr_3 = float(nbr_1) * float(nbr_2)
        print(nbr_3)
    elif ope == "/":
        if float(nbr_2) == 0:
            print("Error, division by zero")
            time.sleep(2)
            os.system('cls')
            calc()
            return
        nbr_3 = float(nbr_1) / float(nbr_2)
        print(nbr_3)
    elif ope == "AC" or ope == "ac":
        os.system('cls')
        calc()
    elif ope == "C":
        ft_ope(nbr_1, nbr_2)
    return nbr_3

def input_1():
    while True:
        nbr_1 = input("Enter the first number: ")
        if nbr_1 == "AC" or nbr_1 == "ac":
            os.system('cls')
            calc()
        elif nbr_1 == "exit":
            return None
        elif nbr_1 is None or not is_float(nbr_1):
            print("Error, invalid first number")
        else:
            return nbr_1

def input_2():
    while True:
        nbr_2 = input("Enter the second number: ")
        if nbr_2 == "AC" or nbr_2 == "ac":
            os.system('cls')
            calc()
        elif nbr_2 == "exit":
            return None
        elif nbr_2 is None or not is_float(nbr_2):
            print("Error, invalid second number")
        else:
            return nbr_2

def is_float(nbr):
    try:
        float(nbr)
        return True
    except ValueError:
        return False

def calc():
    nbr_1 = 0
    print(nbr_1)
    nbr_1 = input_1()
    if nbr_1 is None:
        return
    if nbr_1 == "AC" or nbr_1 == "ac":
        os.system('cls')
        calc()
    if nbr_1 is None or not is_float(nbr_1):
        print("Error, invalid first number")
        return

    while True:
        nbr_2 = input_2()
        if nbr_2 == "AC" or nbr_2 == "ac":
            os.system('cls')
            calc()
        if nbr_2 is None:
            return
        if nbr_2 is None or not is_float(nbr_2):
            print("Error, invalid second number")
            continue
        nbr_1 = ft_ope(nbr_1, nbr_2)
        if nbr_1 is None:
            return

def main():
    os.system('cls')
    title()
    time.sleep(2)
    os.system('cls')
    calc()

if __name__ == "__main__":
    main()
