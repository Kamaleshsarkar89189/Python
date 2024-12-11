# Read write operation in file.

# Writing to a file
def write_to_file(filename, content):
    with open(filename, 'w') as file:  # 'w' mode overwrites the file
        file.write(content)
    print(f"Content written to {filename}")

# Example usage
filename = "example.txt"
content = "Hello, this is a test file.\nWelcome to file operations in Python!"
write_to_file(filename, content)


# Reading from a file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:  # 'r' mode is for reading
            content = file.read()
        print(f"Content of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

# Example usage
read_from_file(filename)
