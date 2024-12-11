# Remove duplicate values from a list of integers by using a function.

def remove_duplicates(int_list):
    # Convert the list to a set to remove duplicates and convert it back to a list
    return list(set(int_list))

# Input: List of integers from the user
user_input = input("Enter a list of integers separated by spaces: ")
int_list = list(map(int, user_input.split()))

# Call the function and display the result
unique_list = remove_duplicates(int_list)
print(f"List after removing duplicates: {unique_list}")
