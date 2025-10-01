file = 'example.txt'

with open(file, 'r', ) as fe:
    text = fe.read()


    lines = len(text.splitlines())
    words = len(text.split())
    characters = len(text)

    print("Lines:", lines)
    print("Words:", words)
    print("Characters:", characters)
