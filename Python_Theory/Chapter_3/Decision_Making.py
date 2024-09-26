# Python - Decision Making

# if...else statement
num = int(input("Enter the number : "))
if (num == 100):
    print("Value of num is equal to 100")
else:
    print("Value of num is not equal to 100")


# # Nested if statements

var = 100 #int(input("Enter the number : "))
if ( var == 100 ):
    print("The number is equal to 100")
    if var % 2 == 0:
        print("The number is even")
    else:
        print("The given number is odd")
elif var == 0:
    print("The given number is Zero")
else:
    print("The given number is negetive")