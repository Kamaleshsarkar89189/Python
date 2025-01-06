# Python - The try-except Block

'''
try and except in Python
The try and except block in Python is used for handling exceptions (errors) during program execution. It allows you to manage errors gracefully without terminating the program unexpectedly.'''

# Example 1: Basic try-except Block

try:
    num = int(input("Enter a number: "))
    print(f"The square of {num} is {num ** 2}")
except ValueError:
    print("Invalid input! Please enter a valid number.")

# Example 2: Handling Multiple Exceptions

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")


# Example 3: Using else and finally

try:
    file = open("example56.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
finally:
    print("Execution complete.")

# Raising Exceptions in Python
# In Python, you can explicitly raise an exception using the raise keyword. This is useful for signaling errors in your code when specific conditions are not met.

# Example 1: Basic Exception Raising

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Example 2: Raising Custom Exceptions

# You can define and raise custom exceptions by creating a subclass of the built-in Exception class.

class NegativeNumberError(Exception):
    """Exception raised for negative numbers."""
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return num ** 0.5

try:
    print(square_root(-4))
except NegativeNumberError as e:
    print(f"Error: {e}")
