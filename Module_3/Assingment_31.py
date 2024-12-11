# Count number of lines and word in a file.

def count_lines_and_words(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines
            num_lines = len(lines)  # Count the number of lines
            num_words = sum(len(line.split()) for line in lines)  # Count words in each line
            
        print(f"File: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the name of the file: ")
count_lines_and_words(filename)
