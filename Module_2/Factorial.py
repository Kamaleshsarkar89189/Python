# def factorial_loop(n):
#     result = 1
#     if num<0:
#         print("Enter a positive number.")
#         exit()
#     else:
#         for i in range(1, n + 1):
#             result *= i
#     return result

# # Example
# num = int(input("Enter number: "))



# print(factorial_loop(num))  # Output: 120


n=int(input("Enter a number "))
d=1
if n<0 :
    print("Enter the number gather than 0")
    exit()
elif n==0 or n==1 :
    print("The factorial is 1")
    exit()
else :
    
    for i in range(1,n+1) :
        d=d*i
    print(f"The factorial of {n} is {d}")