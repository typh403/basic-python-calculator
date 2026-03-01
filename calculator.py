"""
Simple Calculator
D Starter Class - Foundational Python Projects
"""

import sys

def calculator():
    print("Calculator")
    print("Addition +")
    print("Subtraction -")
    print("Multiplication *")
    print("Division /")

    print("Select operation type (e.g., +, -, *, /): ")
    operation = input().strip()

    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation type. Please choose from +, -, *, /.")
        return
    
    print("Enter the first number: ")
    try:
        num1 = float(input().strip())
    except ValueError:
        print("Invalid number. Please enter a valid numeric value.")
        return
        
    print("Enter the second number: ")
    try:
        num2 = float(input().strip())
    except ValueError:
        print("Invalid number. Please enter a valid numeric value.")
        return

    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    calculator()