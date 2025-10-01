# variable parameters or arguments

def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")
