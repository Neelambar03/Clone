# Demonstrating input and type conversion in Python

# Example 1: Reading input as a string
varname = input("Enter a value: ")
print("You entered:", varname)
print("Type of varname:", type(varname))

# Example 2: Reading input and converting to integer
b = input("Enter a number: ")
c = int(b)  # Convert string input to integer
print("You entered:", c)
print("Type of c:", type(c))

# Example 3: Directly converting input to integer
# b = int(input("Enter another number: "))
# print("You entered:", b)
# print("Type of b:", type(b))