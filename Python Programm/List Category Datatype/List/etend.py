l1=[2,4,6,8]
l2=["A", "B", "Q"]
print(l1.extend(l2))  # Extend l1 with l2
# Output: None (extend modifies the list in place)

print(l1)  # Output: [2, 4, 6, 8, "A", "B", "Q"]
print(l2)  # Output: ["A", "B", "Q"]

# We can use the '+' operator to extend
l3 = l2 + l1
print(l3)  # Output: ["A", "B", "Q", 2, 4, 6, 8, "A", "B", "Q"]


l4 = l1 + l2
print(l4) 