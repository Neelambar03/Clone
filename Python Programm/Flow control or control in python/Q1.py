# Write a Python program to accept three integer values and find the biggest among them.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print(f"Values of a, b, c: {a}, {b}, {c}")

if a >= b and a >= c:
    print(f"The biggest number is: {a}")
elif b >= a and b >= c:
    print(f"The biggest number is: {b}")
else:
    print(f"The biggest number is: {c}")
