#  Write a program in Python to print following pattern.

'''
                    1
                2   2   2
            3   3   3   3   3


'''

# Number of rows for the pattern
n = 3

# Loop through each row
for i in range(1, n+1):
    # Printing leading spaces for alignment
    print("  " * (n - i), end="")
    
    # Printing the number corresponding to the row
    for j in range(2 * i - 1):
        print(i, end=" ")
    
    # Move to the next line after each row
    print()
