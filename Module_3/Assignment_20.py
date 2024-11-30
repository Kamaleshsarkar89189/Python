# Write a Python script to find a number is armstrong or not.

# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to access individual digits
    digits = str(number)
    # Calculate the sum of each digit raised to the power of the number of digits
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    # Check if the sum is equal to the original number
    return total == number

# Input: User-provided number
try:
    num = int(input("Enter a number to check if it is an Armstrong number: "))
    
    # Check if the number is an Armstrong number
    if is_armstrong(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
except ValueError:
    print("Please enter a valid integer.")
