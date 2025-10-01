# write a python function program which can accept the student record as an positional argument and names variable length argument and subject as default argument

def student_record(student, *names, subject="Mathematics"):
	print(f"Student Record: {student}")
	print("Names:", ", ".join(names))
	print(f"Subject: {subject}")
	
# Example usage
student_record("John Doe", "Alice", "Bob", "Charlie", subject="Science")
student_record("Jane Smith", "David", "Eve")
