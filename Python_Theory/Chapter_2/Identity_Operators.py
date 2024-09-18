# Python - Identitiy Operators
# Python Identity Operators
    # * 'is' Operator
    # * 'is not' Operator

# Python 'is' Operator

    # The 'is' operator evaluates to True if both the operand objects share the same memory location. The memory location of the object can be obtained by the "id()" function. If the "id()" of both variable is same, the "is" operator returns True.

# Example 

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a
# comparing and printing return values
print(a is c)
print(a is b)

# Printing IDs of a, b, and c 
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c)) 