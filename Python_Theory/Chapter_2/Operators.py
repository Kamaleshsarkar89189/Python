# Python - Operators

'''Python operators are special symbols used to perform specific operations on one or more operands.'''

# Types of Python Operators

''' * Arithmetic Operators
    * Comparision (Relational) Operators
    * Assignment Operators
    * Logical Operators
    * Bitwise Operators
    * Membership Operators
    * Identity Operators
'''

# Python Arithmetic Operators

'''     Operator	Name	        Example
            +	    Addition	    a + b = 30
            -	    Subtraction	    a – b = -10
            *	    Multiplication	a * b = 200
            /	    Division	    b / a = 2
            %	    Modulus	        b % a = 0
            **	    Exponent	    a**b =10**20
            //	    Floor Division	9//2 = 4
'''

a = 21
b = 10
c = 0
c = a+b
print("a: {} b: {} a+b: {}".format(a,b,c))

# Python Comparison Operators

'''     Operator	        Name	                    Example
            ==	            Equal	                    (a == b) is not true.
            !=	            Not equal	                (a != b) is true.
            >	            Greater than                (a > b) is not true.
            <	            Less than	                (a < b) is true.
            >=	            Greater than or equal to	(a >= b) is not true.
            <=	            Less than or equal to       (a <= b) is true.'''

# Example of Python comparison Operators

a = 21
b = 10
if ( a == b ):
   print ("Line 1 - a is equal to b")
else:
   print ("Line 1 - a is not equal to b")

if ( a != b ):
   print ("Line 2 - a is not equal to b")
else:
   print ("Line 2 - a is equal to b")

if ( a < b ):
   print ("Line 3 - a is less than b" )
else:
   print ("Line 3 - a is not less than b")

if ( a > b ):
   print ("Line 4 - a is greater than b")
else:
   print ("Line 4 - a is not greater than b")

a,b=b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
   print ("Line 5 - a is either less than or equal to  b")
else:
   print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
   print ("Line 6 - b is either greater than  or equal to b")
else:
   print ("Line 6 - b is neither greater than  nor equal to b")