import os
import Calculator_art

def clear():
    os.system("cls")

def outer():
    num1 = int(input("What's the first number?: "))
    print('''
    +
    -
    *
    /
    ''')
    return num1

def inner(num1):
        operation = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        
        if operation == "+" :
            return num1 + num2
            
        elif operation == "-":
            return num1 - num2
            
        elif operation == "*":
            return num1 * num2
            
        elif operation == "/":
            return num1 / num2
            
        else:
            print("Invalid operation")


print(Calculator_art.logo)
answer = inner(outer())
cont = False

while not cont:
    
    process = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

    if process == "y":
        answer = inner(answer)
        cont = False
        continue
    elif process == "n":
        clear()
        cont = False
        print(Calculator_art.logo)
        answer = inner(outer())
        continue
    else:
        cont = True
        print("Invalid input")
