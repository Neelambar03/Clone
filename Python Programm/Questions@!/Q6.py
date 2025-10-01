# Q. Write a Python program that uses the filter function to find all the palindromes in a list of strings. A palindrome is a word that reads the same backward as forward (e.g., "radar", "level", "madam").

from typing import List

# Importing necessary module

# Function to check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# List of strings
strings = ["radar", "hello", "level", "world", "madam", "python"]

# Using filter to find palindromes
palindromes = list(filter(is_palindrome, strings))

# Output the result
print("Palindromes in the list:", palindromes)