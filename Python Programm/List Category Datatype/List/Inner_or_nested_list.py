li = [2, ["phy", "chem", "math", "pyth", "hindi", "dsa"], ["m", "f"], 83.5]

# Print the second element of the list
print(li[1])  # Output: ['phy', 'chem', 'math', 'pyth', 'hindi', 'dsa']

# Print the fourth element of the second list
print(li[1][4])  # Output: 'math'

# Print a slice of the third list
print(li[2][-2:])  # Output: ['m', 'f']

# Print a slice of the second list
print(li[1][-3:-1])  # Output: ['pyth', 'hindi']

# Print the last element of the second-to-last list
print(li[-2][-1])  # Output: 'f'

# Append a new element to the second list
li[1].append("A")
print(li)  # Output: [2, ['phy', 'chem', 'math', 'pyth', 'hindi', 'dsa', 'A'], ['m', 'f'], 83.5]
