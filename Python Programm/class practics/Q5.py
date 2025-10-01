# write a python program of factroial of given input number if a input no. is less than 1 if a decimal point value.


import math

def factorial_of_number(num):
    if num < 1 or not num.is_integer():
        return "Input must be a positive integer."
    else:
        return math.factorial(int(num))

try:
    user_input = float(input("Enter a number: "))
    result = factorial_of_number(user_input)
    print(result)
except ValueError:
    print("Invalid input. Please enter a numeric value.")