# Write a python program which an accept the student record as an positional argument and mark variable length argument and subject as an default argument.

# Ans:

# Define a function to accept student records with positional, variable-length, and default arguments
def stu(Name, Roll, *y, Subject="Python"):
    print(Name)
    print(Roll)
    for i in y:
        print(i)
    print(Subject)

# Example usage:
stu("Song", 5, 20, 40, 60, 80)
