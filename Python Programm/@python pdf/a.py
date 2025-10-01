# Attempt to open and read the file
try:
    with open('a.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: 'a.txt' not found.")
