# write a program take two number and return the sum of no. by using function call in python

def add_numbers(a, b):
    return a + b

# Get two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to add the numbers
result = add_numbers(num1, num2)

# Print the result
print("The sum is:", result)

