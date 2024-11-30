#Write a Python Program to find the sum of s = 1-x+x²⁄2!-x³/3!+...

import math

# Function to calculate the sum of the series
def calculate_series(x, n):
    series_sum = 0
    for i in range(n + 1):  # Iterate from 0 to n
        term = ((-1) ** i) * (x ** i) / math.factorial(i)  # Calculate each term
        series_sum += term
    return series_sum

# Input: User-provided x and n
try:
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the number of terms (n): "))
    
    if n < 0:
        print("The number of terms (n) should be a non-negative integer.")
    else:
        # Calculate the series sum
        result = calculate_series(x, n)
        # Display the result
        print(f"The sum of the series is: {result}")
except ValueError:
    print("Please enter valid numeric inputs for x and n.")
