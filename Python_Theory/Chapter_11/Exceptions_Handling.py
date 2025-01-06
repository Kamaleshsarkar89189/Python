# Python - Exceptions Handling
'''
Exception handling in Python refers to managing runtime errors that may occur during the execution of a program.
'''

# assert in Python

# The assert statement in Python is a debugging aid that tests a condition as part of your code. It checks whether a given condition evaluates to True. If the condition is False, the program raises an AssertionError exception and optionally outputs an error message.


# Example

# Example of using assert
def divide(a, b):
    assert b != 0, "Denominator cannot be zero."
    return a / b

print(divide(10, 2))  # Outputs: 5.0
print(divide(10, 0))  # Raises AssertionError: Denominator cannot be zero.
