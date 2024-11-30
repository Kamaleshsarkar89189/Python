#Write a Python script to find a number is neon number or not.

# Function to check if a number is a Neon number
def is_neon(number):
    # Calculate the square of the number
    square = number ** 2
    # Calculate the sum of the digits of the square
    digit_sum = sum(int(digit) for digit in str(square))
    # Check if the sum of the digits is equal to the original number
    return digit_sum == number

# Input: User-provided number
try:
    num = int(input("Enter a number to check if it is a Neon number: "))
    
    # Check if the number is a Neon number
    if is_neon(num):
        print(f"{num} is a Neon number.")
    else:
        print(f"{num} is not a Neon number.")
except ValueError:
    print("Please enter a valid integer.")
