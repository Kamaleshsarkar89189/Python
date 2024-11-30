#Write a Python Program to find the sum of s = 0+1+2+3+4+...+(upto n term)

# Function to calculate the sum of the series
def calculate_sum(n):
    # Formula for the sum of first n integers
    return n * (n + 1) // 2

# Input: User-provided number of terms
try:
    n = int(input("Enter a non-negative integer (n) to calculate the sum of the series: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        # Calculate the sum
        result = calculate_sum(n)
        # Display the result
        print(f"The sum of the series 0 + 1 + 2 + ... + {n} is: {result}")
except ValueError:
    print("Please enter a valid integer.")
