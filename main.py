############################################################################
#                           MAKE BY LouisVDE 		                       #
############################################################################

import os # IMPORT OS FOR CLEAR SCREEN
import time # IMPORT TIME FOR SLEEP
import platform # IMPORT PLATFORM FOR CHECK OS

# Clear the screen
def clear_screen():
    # CHECK OS
    if platform.system() == 'Windows': # IF OS IS WINDOWS
        os.system('cls')
    else: # IF OS IS NOT WINDOWS
        os.system('clear')

# Title
def title():
    purple = '\033[95m' # PURPLE CODE COLOR
    reset = '\033[0m' # RESET COLOR
    text = '''      _____      _            _       _             
     / ____|    | |          | |     | |            
    | |     __ _| | ___ _   _| | __ _| |_ ___  _ __ 
    | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
    | |___| (_| | | (__| |_| | | (_| | || (_) | |   
     \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   '''
    print(purple + text + reset)
    print("            Version 1.2   by LouisVDE")

# Operations
def ft_ope(nbr_1, nbr_2):
    nbr_3 = 0
    ope = input("Enter an operator: ")
    if ope == "exit": # Exit
        return None
    if ope not in ["+", "-", "*", "/", "AC", "ac"]: # CHECK IF OPERATOR IS VALID
        print("Error, invalid operator")
        return
    if ope == "+": # ADDITION
        nbr_3 = float(nbr_1) + float(nbr_2)
        print(nbr_3)
    elif ope == "-": # SUBTRACTION
        nbr_3 = float(nbr_1) - float(nbr_2)
        print(nbr_3)
    elif ope == "*": # MULTIPLICATION
        nbr_3 = float(nbr_1) * float(nbr_2)
        print(nbr_3)
    elif ope == "/": # DIVISION
        if float(nbr_2) == 0: # CHECK IF DIVISION BY ZERO
            print("Error, division by zero") # ERROR
            time.sleep(2)
            clear_screen()
            calc()
            return
        nbr_3 = float(nbr_1) / float(nbr_2)
        print(nbr_3)
    elif ope == "AC" or ope == "ac": # RESET CALCULATOR
        clear_screen()
        calc()
    elif ope == "C": 
        ft_ope(nbr_1, nbr_2)
    return nbr_3

# TAKE THE FIRST NUMBER
def input_1():
    while True:
        nbr_1 = input("Enter the first number: ")
        if nbr_1 == "AC" or nbr_1 == "ac": # RESET CALCULATOR
            clear_screen()
            calc()
        elif nbr_1 == "exit": # EXIT
            return None
        elif nbr_1 is None or not is_float(nbr_1): # CHECK IF NUMBER IS VALID
            print("Error, invalid first number")
        else:
            return nbr_1

# TAKE THE SECOND NUMBER
def input_2():
    while True:
        nbr_2 = input("Enter the second number: ")
        if nbr_2 == "AC" or nbr_2 == "ac": # RESET CALCULATOR
            clear_screen()
            calc()
        elif nbr_2 == "exit": # EXIT
            return None
        elif nbr_2 is None or not is_float(nbr_2): # CHECK IF NUMBER IS VALID
            print("Error, invalid second number")
        else:
            return nbr_2

# CHECK IF NUMBER IS VALID
def is_float(nbr):
    try: # CHECK IF NUMBER IS FLOAT
        float(nbr) 
        return True # IF NUMBER IS FLOAT
    except ValueError:
        return False # IF NUMBER IS NOT FLOAT

# CALCULATOR
def calc():
    nbr_1 = 0 # INIT FIRST NUMBER
    print(nbr_1)
    nbr_1 = input_1() # TAKE FIRST NUMBER
    if nbr_1 is None: # IF NUMBER IS NONE
        return # RETURN
    if nbr_1 == "AC" or nbr_1 == "ac": # RESET CALCULATOR
        clear_screen()
        calc()
    if nbr_1 is None or not is_float(nbr_1): # CHECK IF NUMBER IS VALID
        print("Error, invalid first number") # IF NUMBER IS NOT VALID
        return # RETURN
    while True:
        nbr_2 = input_2() # TAKE SECOND NUMBER
        if nbr_2 == "AC" or nbr_2 == "ac": # RESET CALCULATOR
            clear_screen()
            calc()
        if nbr_2 is None: # IF NUMBER IS NONE
            return # RETURN
        if nbr_2 is None or not is_float(nbr_2): # CHECK IF NUMBER IS VALID
            print("Error, invalid second number") # IF NUMBER IS NOT VALID
            continue # CONTINUE
        nbr_1 = ft_ope(nbr_1, nbr_2) # DO OPERATION
        if nbr_1 is None:
            return

# MAIN
def main():
    clear_screen() # CLEAR SCREEN
    title() # PRINT TITLE
    time.sleep(2) # WAIT 2 SECONDS
    clear_screen() # CLEAR SCREEN
    calc() # START CALCULATOR

# START MAIN
if __name__ == "__main__":
    main()
