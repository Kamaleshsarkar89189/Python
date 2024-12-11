# Write a program in Python to print following pattern
'''
            A   A   A   A
               B  B   B
                C   C  
                  D

'''

# Number of rows for the pattern
n = 4

# Loop through each row
for i in range(n):
    # Printing leading spaces for alignment
    print(" " * i, end="")
    
    # Printing the letter corresponding to the row
    for j in range(n - i):
        print(chr(65 + i), end=" ")
    
    # Move to the next line after each row
    print()
