# Write a Python Script to implement linear search in a user inputted list of integers.

# Function to perform linear search
def linear_search(num_list, target):
    for index, value in enumerate(num_list):
        if value == target:
            return index  # Return the index where the target is found
    return -1  # Return -1 if the target is not found

n = int(input("Enter the number of elements in the list: "))
num_list = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    num_list.append(element)
target = int(input("Enter the number to search for: "))
result = linear_search(num_list, target)
if result != -1:
    print(f"Number found at index {result}")
else:
    print("Number not found in the list")
