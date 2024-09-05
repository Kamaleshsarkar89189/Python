# swap without 3rd variable

a=int(input("enter the value of  a "))
b=int(input("enter the value of  b "))
a,b=b,a
print("the value of a is",a,"and the value of b is",b)

# Swap with 3rd varible
a=int(input("enter the value of  a "))
b=int(input("enter the value of  b "))
a,b=b,a
print("the value of a is",a,"and the value of b is",b)

# Swap with swap function
'''
def swap(a, b):
    a, b = b, a
    return a, b
a=int(input("enter the value of  a "))
b=int(input("enter the value of  b "))
a,b=swap( a, b)
print("the value of a is",a,"and the value of b is",b)
'''