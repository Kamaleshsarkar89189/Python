#Write a Python Program to find the sum of s = 1+x+x²+x³+...+ xⁿ

# Function to calculate the sum of the series
def calculate_series(x, n):
    if x == 1:
        # Special case: when x = 1
        return n + 1
    else:
        # General formula for GP sum
        return (1 - x**(n + 1)) / (1 - x)

# Input: User-provided values for x and n
try:
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the value of n (highest exponent): "))
    
    if n < 0:
        print("Please enter a non-negative integer for n.")
    else:
        # Calculate the series sum
        result = calculate_series(x, n)
        # Display the result
        print(f"The sum of the series is: {result}")
except ValueError:
    print("Please enter valid numeric inputs for x and n.")
