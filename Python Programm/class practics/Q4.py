try:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("Addition:", add(num1, num2))
    print("Subtraction:", subtract(num1, num2))
    print("Multiplication:", multiply(num1, num2))
    print("Division:", divide(num1, num2))

except TypeError:
    print("Invalid input! Please enter numeric values.")

except ZeroDivisionError:
    print("if b=0, Invalid ")

except IndentationError:
    print("Indentation Error")
