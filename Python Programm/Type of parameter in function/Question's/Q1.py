# Q. write a Python program that demonstrates the use of positional, keyword, and default arguments to enter student record data.

def enter_student_record(name, age, grade="Not Assigned", school="Unknown"):
    print(f"Student Name: {name}")
    print(f"Age: {age}")
    print(f"Grade: {grade}")
    print(f"School: {school}")

# Using positional arguments
enter_student_record("Alice", 14)

# Using positional and keyword arguments
enter_student_record("Bob", 15, grade="9th")

# Using all keyword arguments
enter_student_record(name="Charlie", age=16, grade="10th", school="High School")

# Using default arguments
enter_student_record("Diana", 13, school="Middle School")