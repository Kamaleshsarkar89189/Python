# Write a python program to perform read write operation on the file.

# Program to perform read and write operations on a file

def write_to_file(filename, content):
    """Writes content to a file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content written to {filename} successfully.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def read_from_file(filename):
    """Reads content from a file."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content read from {filename} successfully:")
        print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    # File name to perform operations on
    filename = "example.txt"
    
    # Content to write to the file
    content = "Hello, World!\nThis is a simple file operation example in Python."
    
    # Write operation
    write_to_file(filename, content)
    
    # Read operation
    read_from_file(filename)

if __name__ == "__main__":
    main()


# write a program in python to create a class student with the attribute name, age, and grade use the constructor to initialize the defult value and method print _info() to print the value for three objects.

#Write a program in python to demonstrate inheritance create a class called CSE student from class student from class student that has the extra attribute of graduation year, override the function print info to print the details of derived class.

#Write a program in Python 