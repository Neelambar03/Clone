# Initial values
a = 5  # Binary: 0101
b = 3  # Binary: 0011

# Swapping using XOR
a = a ^ b  # a becomes 6 (0110)
b = a ^ b  # b becomes 5 (0101)
a = a ^ b  # a becomes 3 (0011)

print("After swapping:")
print("a =", a)
print("b =", b)
