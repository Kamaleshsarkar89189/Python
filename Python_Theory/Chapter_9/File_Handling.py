# Python - File Handling

# Opening a File in Python

    # Syntax
file = open("filename", "mode")

# File Opening Modes

'''
    r : Opens a file for reading only.
    r+ : Opens a file for both reading and writing.

    w : Opens a file for writing only.
    w+ : Opens a file for both writing and reading.

    a : Opens a file for appending.
    a+ : Opens a file for both appending and reading.

    w : Opens a file for writing only.
    w+ : Opens a file for both writing and reading.

    b : Opens the file in binary mode
 '''

# Reading a File in Python

    # read() − Reads the entire file.

    # readline() − Reads one line at a time.

    # readlines − Reads all lines into a list.

# Closing a File in Python

file = open("examples.txt", "w")
file.write("This is an example.")
file.close()
print ("File closed successfully!!")

# Using "with" Statement for Automatic File Closing

with open("exampless.txt", "w") as file:
   file.write("This is an example using the with statement.")
   print ("File closed successfully!!")