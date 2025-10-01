# Q4. Write a Python program to read a text file and print its contents line by line.
with open ('example.txt', "r") as f:
   for line in f:
       print(line.strip())
  



