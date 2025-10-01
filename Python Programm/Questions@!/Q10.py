def factorial(n):
    """
    Calculate the factorial of a number using recursion.

    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a number to find its factorial: "))
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"The factorial of {number} is {factorial(number)}")