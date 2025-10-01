try:
    with open("a.txt", "r") as file:
        content = file.read()
        print("File Contents:")
        print(content)
except FileNotFoundError:
    print("Error: The file 'a.txt' does not exist.")