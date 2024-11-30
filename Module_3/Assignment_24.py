# Write a Python Program to find the sum of s = 1 + (1 + 2) + (1 + 2 +3) + ...+ (1+2+3+..n)


# Function to calculate the sum of the series
def calculate_series(n):
    series_sum = 0
    for k in range(1, n + 1):
        series_sum += (k * (k + 1)) // 2  # Sum of the first k natural numbers
    return series_sum

# Input: User-provided number of terms
try:
    n = int(input("Enter the value of n (number of terms): "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        # Calculate the series sum
        result = calculate_series(n)
        # Display the result
        print(f"The sum of the series is: {result}")
except ValueError:
    print("Please enter a valid integer.")
