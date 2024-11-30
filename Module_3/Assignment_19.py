# Write a Python script to implement linear search in a user inputted list of integers.

# Linear search implementation
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Input: User-provided list of integers
try:
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    # Input: Target number to search
    target = int(input("Enter the number to search for: "))
    
    # Perform linear search
    result = linear_search(numbers, target)
    
    # Output the result
    if result != -1:
        print(f"The number {target} is found at index {result}.")
    else:
        print(f"The number {target} is not found in the list.")
except ValueError:
    print("Please ensure all inputs are valid integers.")
