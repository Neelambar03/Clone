# Syntax: filter(function_name, iterable_object)

numbers = [-2, 3, -5, 6, 7, 8]
neg = list(filter(lambda x: x < 0, numbers))
print(neg)  # Output: [-2, -5]



