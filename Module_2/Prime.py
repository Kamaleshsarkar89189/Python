def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False
    
    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is prime or non-prime
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a non-prime number.")