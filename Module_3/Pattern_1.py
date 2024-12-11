# Write a program in Python to print the following pattern

'''
                    1
                2   1   2
            3   2   1   2   3


'''


# Number of rows for the pattern
n = 3

# Loop through each row
for i in range(1, n+1):
    # Printing leading spaces for alignment
    print("  " * (n - i), end="")
    
    # Printing decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    # Printing increasing numbers
    for j in range(2, i+1):
        print(j, end=" ")
    
    # Move to the next line after each row
    print()
