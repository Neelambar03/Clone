l1 = [2, 4, 6, 7, 8]
del l1
# print(l1)  # This will raise an error because l1 is deleted

l1 = [2, 4, 6, 7, 8]
del l1[0]
print(l1)  # Output: [4, 6, 7, 8]

del l1[0:2]
print(l1)  # Output: [7, 8]
