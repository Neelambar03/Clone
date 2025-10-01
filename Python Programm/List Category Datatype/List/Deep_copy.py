l1=[2,4,6,7,8]
L2=l1
print(l1, L2)
print(id(l1), id(L2))
xy = 'example_value'  # Define the variable xy
l1.append(xy)
print(l1, L2)  # Output: [2, 4, 6, 7, 8, 'example_value'], [2, 4, 6, 7, 8, 'example_value']
