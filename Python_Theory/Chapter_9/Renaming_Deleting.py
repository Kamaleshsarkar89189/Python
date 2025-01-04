# Python - Renaming and Deleting Files

# In Python, you can rename and delete files using built-in functions from the os module.

# Renaming Files in Python

import os

# Current file name
current_name = "oldfile.txt"

# New file name
new_name = "newfile.txt"

# Rename the file
os.rename(current_name, new_name)

print(f"File '{current_name}' renamed to '{new_name}' successfully.")

# Deleting Files in Python

import os

# File to be deleted
file_to_delete = "file_to_delete.txt"

# Delete the file
os.remove(file_to_delete)

print(f"File '{file_to_delete}' deleted successfully.")