# keyword variable lengths or argument

def greet(*, name, message):
    print(f"{message}, {name}!")

greet(name="Alice", message="Hello")
