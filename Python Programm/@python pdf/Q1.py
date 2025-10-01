try:
   
    file_name = "output's.txt"
    
   
    with open(file_name, "w") as file:
        
        file.write("Hello, this is a sample text written to the file.")
        file.write("This program handles any IO errors that might occur.")
    print(f"Text successfully written to {file_name}.")
except IOError as e:
    
    print(f"An IOError occurred: {e}")