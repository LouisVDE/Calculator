import os
import time

def ft_ope(nbr_1, nbr_2):
    nbr_3 = 0
    ope = input("Enter an operator: ")
    if ope not in ["+", "-", "*", "/", "AC", "ac"]:
        print("Error, invalid operator")
        exit()
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
        nbr_3 = float(nbr_1) / float(nbr_2)
        print(nbr_3)
    elif ope == "AC" or ope == "ac":
        os.system('clear')
        calc()
    elif ope == "C":
        ft_ope(nbr_1, nbr_2)
    return nbr_3

def input_1():
    nbr_1 = input("Enter the first number: ")
    if nbr_1 == "AC" or nbr_1 == "ac":
        os.system('clear')
        calc()
    elif nbr_1 == "exit":
        exit()
    elif not is_float(nbr_1):
        print("Error, invalid first number")
        exit()
    return nbr_1
     
def input_2():
    nbr_2 = input("Enter the second number: ")
    if nbr_2 == "AC" or nbr_2 == "ac":
        os.system('clear')
        calc()
    elif nbr_2 == "exit":
        exit()
    elif not is_float(nbr_2):
        print("Error, invalid second number")
        exit()
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
    if nbr_1 == "AC" or nbr_1 == "ac":
        os.system('clear')
        calc()
    if nbr_1 == "exit":
        exit()
    if not is_float(nbr_1):
        print("Error, invalid first number")
        exit()

    while True:
        nbr_2 = input_2()
        if nbr_2 == "AC" or nbr_2 == "ac":
            os.system('clear')
            calc()
        if not is_float(nbr_2):
            print("Error, invalid second number")
            exit()
        nbr_1 = ft_ope(nbr_1, nbr_2)

def main():
    os.system('clear')
    print("Welcome to the calculator")
    time.sleep(2)
    os.system('clear')
    calc()

if __name__ == "__main__":
    main()
