import Calculator_art
import os

def clear():
    os.system("cls")

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiplication, 
    "/": division,
    }

def calculator():
    print(Calculator_art.logo)
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_calculation = True

    while continue_calculation:
        operation = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_op = operations[operation]
        answer = calculation_op(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
            continue_calculation = True
        else:
            continue_calculation = False
            clear()
            calculator()

calculator()