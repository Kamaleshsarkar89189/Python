# Write a python program to reverse a string.

def reverse_string (s) :
    return s[::-1]

input_string = "Hello world!"
reversed_string=reverse_string(input_string)
print(f"The reversed string is : {reversed_string}")