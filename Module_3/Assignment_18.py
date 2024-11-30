# Write a python program to create list of integers and count the number of integer ending with 5.

# Create a list of integers
numbers = [10, 15, 25, 35, 40, 50, 65, 75, 85, 90]

# Count integers ending with 5
count = sum(1 for num in numbers if str(num).endswith('5'))

# Display the result
print(f"The number of integers ending with 5: {count}")
