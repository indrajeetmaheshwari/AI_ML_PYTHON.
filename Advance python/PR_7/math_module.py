import math

def factorial():
    n = int(input("Enter number to find its factorial : "))
    print("Factorial of number ", n , "is", math.factorial(n))

def compound_interest():
    intrest_percentage = float(input("Enter intrest percentage: "))
    rate = float(input("Enter rate: "))
    time = float(input("Enter time: "))
    compound_int = intrest_percentage * (1 + rate/100) ** time
    print("Compound Interest:", compound_int)