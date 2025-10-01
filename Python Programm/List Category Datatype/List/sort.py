# l1 = [2, 4, 6, 'A', "ABC", 2.6]
# l2=l1.short()                                   
# try:
#     print(l2)
# except NameError as e:
#     print("Error:", e)
                                                           
# Question 2
l1 = [2, 4, 8, 3, 2, 1, 7]
l2 = sorted(l1)  # Sorts the list without modifying the original
print("l2:", l2)

l3 = list(reversed(l2))  # Reverses the sorted list
print("l3:", l3)

l4 = sorted(l1, reverse=True)  # Sorts the list in descending order
print("l4:", l4)

I5 = (id(l1), id(l2))  # Gets the memory addresses of l1 and l2
print("I5:", I5)
