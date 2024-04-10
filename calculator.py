from replit import clear
import calculator_art

print(calculator_art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(n1, n2, operation):
    if operation == "+":
        return add(n1, n2)
    elif operation == "-":
        return subtract(n1, n2)
    elif operation == "*":
        return multiply(n1, n2)
    elif operation == "/":
        return divide(n1, n2)
        
number1 = float(input("What's the first number?: "))
print("+\n-\n*\n/")
operation = input("Pick an operation: ")
number2 = float(input("What's the next number?: "))

result = calculate(number1, number2, operation)
print(f"{number1} {operation} {number2} = {result}")

choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'e' to exit: ")    

while choice != "e":
    if choice == "y":
        clear()
        print(calculator_art.logo)
        print(f"{result}")
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        result = calculate(result, number2, operation)
        print(f"{number1} {operation} {number2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'e' to exit: ")
    else:
        clear()
        print(calculator_art.logo)
        number1 = float(input("What's the first number?: "))
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        result = calculate(number1, number2, operation)
        print(f"{number1} {operation} {number2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or 'e' to exit: ")

print("Goodbye!")
