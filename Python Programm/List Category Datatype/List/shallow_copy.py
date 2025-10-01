# Example of shallow copy
l1 = [2, 4, 6, 8, 10]
l2 = l1.copy()

print("l1:", l1)
print("l2:", l2)

print("IDs of l1 and l2:")
print(id(l1), id(l2))


l3=[2,4,6,7,8]
l4 = l3[0:5]  # Slicing: 0 = starting point, 5 = end point
print(l3, l4)
# Output: [2, 4, 6, 7, 8], [2, 4, 6, 7, 8]

print("IDs of l3 and l4:")
print(id(l3), id(l4))
# Output: [xy2323], [xy3123]
l3.append("neelambar")
print(l3, l4)
# Output: [2, 4, 6, 7, 8, "neelambar"], [2, 4, 6, 7, 8]


l5 = [2, "neelambar", 4, 8, 9]
l6 = l5[0:3]
print(l5, l6)
# Output:
# l5 = [2, "neelambar", 4, 8, 9]
# l6 = [2, "neelambar", 4]
print(id(l5), id(l6))
# Output: [xy3433], [pg6557]
