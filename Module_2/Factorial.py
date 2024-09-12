def factorial_loop(n):
    result = 1
    if num<0:
        print("Enter a positive number.")
        exit()
    else:
        for i in range(1, n + 1):
            result *= i
    return result

# Example
num = int(input("Enter number: "))



print(factorial_loop(num))  # Output: 120
