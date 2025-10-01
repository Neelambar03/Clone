file = "example.txt"

try:
    with open(file, 'r') as file:
        if not file.read().strip():
            print("The file is empty.")
except FileNotFoundError:
    print("The file does not exist.")


