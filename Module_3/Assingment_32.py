# Print frequency of each character in file.

def character_frequency(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()  # Read the entire content of the file
            
        # Initialize a dictionary to store frequencies
        freq = {}
        
        for char in content:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Display the frequencies
        print(f"Character frequencies in {filename}:")
        for char, count in freq.items():
            # Replace spaces and newlines for better readability
            display_char = char if char not in [' ', '\n'] else repr(char)
            print(f"'{display_char}': {count}")
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = input("Enter the name of the file: ")
character_frequency(filename)
