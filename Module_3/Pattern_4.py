# Write a program in Python to print following pattern.
'''
    *******
    *     *
    *     *
    *     *
    *******
'''


# Number of rows for the pattern
n = 4

# Loop to print the pattern
for i in range(n):
    # Print the first and last row with all '*' characters
    if i == 0 or i == n - 1:
        print('*' * 7)  # Printing 7 '*' characters for first and last rows
    else:
        print('*' + ' ' * 5 + '*')  # Printing '*' with spaces in between for middle rows
