# Write a python code to caculate and display the sumation of a given eqution.

# ∑ to the power of n

# Define the function for the equation
def equation(n):
    return n^2

# Function to calculate the summation
def summation(N):
    total_sum = 0
    for n in range(1, N + 1):
        total_sum += equation(n)
    return total_sum

# Input from the user
N = int(input("Enter the value of N: "))

# Calculate and display the summation
result = summation(N)
print(f"The summation is: {result}")
