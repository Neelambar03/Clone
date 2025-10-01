source="C:\\Users\\rajku\\OneDrive\\Documents\\Python Programm\\bcd.jpg"
destination = "C:\\Users\\rajku\\OneDrive\\Documents\\a.jpg"

with open(source, 'rb') as fe:
    with open(destination, 'wb') as fe2:
       fe2.write(fe.read())


print("File copied successfully")