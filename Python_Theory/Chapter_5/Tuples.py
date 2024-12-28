# Python - Tuples

# Tuple is one of the built-in data types in Python.


# Python tuple and list both are sequences. One major difference between the two is, Python list is mutable, whereas tuple is immutable. Although any item from the tuple can be accessed using its index, and cannot be modified, removed or added.

# Accessing Values in Tuples


tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])


# Updating Tuples

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)


# Delete Tuple Elements

tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
del tup
print ("After deleting tup : ")
print (tup)


# Built-in Functions with Tuples/
    
'''Sr.No.	Function with Description
    1	    cmp(tuple1, tuple2)
            Compares elements of both tuples.

    2	    len(tuple)
            Gives the total length of the tuple.

    3	    max(tuple)
            Returns item from the tuple with max value.

    4	    min(tuple)
            Returns item from the tuple with min value.

    5	    tuple(seq)
            Converts a list into tuple.'''


