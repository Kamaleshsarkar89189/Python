# Copy content of one file to another file.

def copy_file(source_file, destination_file):
    try:
        # Open the source file for reading
        with open(source_file, 'r') as src:
            content = src.read()  # Read the entire content

        # Open the destination file for writing
        with open(destination_file, 'w') as dest:
            dest.write(content)  # Write the content to the destination file

        print(f"Content copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: {source_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source = input("Enter the name of the source file: ")
destination = input("Enter the name of the destination file: ")
copy_file(source, destination)
