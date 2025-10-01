# Demonstrating the use of the complex() function in Python

# Creating a complex number from a boolean value
print(complex(True))  # Output: (1+0j)
print(complex(False))  # Output: 0j

# Creating a complex number from integers
print(complex(3, 2))  # Output: (3+2j)

# Accessing the real and imaginary parts of a complex number
z = complex(3, 2)
print(z.real)  # Output: 3.0
print(z.imag)  # Output: 2.0

# Creating a complex number from a string
print(complex("12"))  # Output: (12+0j)

# Creating a complex number from a float
print(complex(10.5))  # Output: (10.5+0j)

# Invalid cases (commented out to avoid runtime errors)
# print(complex("Python"))  # Raises ValueError
# print(complex("3x*4y"))   # Raises ValueError
# print(complex(bool("Python")))  # Raises ValueError
