i = 5  # Global variable

def sum():
    global i  # Declare 'i' as global to modify it
    i = i + 1
    return i

# Call the function and print the results
print("sum:", sum())  # Output: 6
print("i:", i)        # Output: 6


i = 5  # Global variable

def sum():
    global i  # Declare 'i' as global to modify it
    j = 2  # Local variable
    i = i + 2
    return i + 2

# Call the function and print the results
print("sum:", sum())  # Output: 9
print("i:", i)        # Output: 7
