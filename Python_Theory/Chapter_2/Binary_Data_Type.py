# Python Binary Data Types
'''A binary data type in Python is a way to represent data as a series of binary digits, which are 0's and 1's. It is like a special language computer understand to store and process information efficiently.

This type of data is commonly used when dealing  with things like files, images, or anything that can be represented using just two possible values.


    Python Provides three different ways to represent binary data. They are as follows -
    
        * bytes
        * bytearray
        * memoryview'''

    # Python Bytes Data Type

        # We can create bytes in Python using built-in bytes() function or by explicitly specify a sequence of numbers with b.


# Using bytes() function to create bytes
b1 = bytes([65, 66, 67, 68, 69])  
print(b1)  


# Using prefix 'b' to create bytes
b2 = b'Hello'  
print(b2)  


# Python Bytearray Data Type

'''The bytearray data type in python is quite similar to the bytes data type, but with one key difference: it is mutable, meaning you can modify the values stored in it after it is created.'''

print("Bytearray Data Type")
# Creating a byte from an iterable of integers
value = bytearray([72, 101, 108, 108, 111])
print(value)


# Creating a bytearray by ending a string
print("bytearray by ending a string")
val = bytearray("Hello", 'utf-8')
print(val)

# Python Memoryview Data Type

'''In Python, a memoryview is a built-in object that provides a view into the memory of the original object, generally objects that support the buffer protocol, such as byte arrays (bytearray) and bytes (bytes). It allows you to access the underlying data of the original object without copying it, providing efficient memory access for large datasets.'''

# Example of Memoryview Data Type

data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

# If you have an array object

import array
arr = array.array('i',[1,2,3,4,5])
view = memoryview(arr)
print(view)

# You can also create a memoryview by slicing a bytes or bytearray object

data = b'Hello, Kamalesh!'
# Creating a view of the last part of the data
view = memoryview(data[7:])
print(view)



# Python Dictionary Data Type

'''Python dictionary are kind of hash table type. A dictionary key can be almost any Python type, but are usually number or strings. Values, on the other hand, can be any arbitrary Python object.'''

# Example of Dictionary Data Type

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


# Python Set Data Type

'''Set is a Python implementation of set as defined in Mathematics. A set in Python is a collection, but is not an indexed or ordered collection as string, list or tuple. An object can't appear more than once in a set, whereas in List and Tuple, same object can appear more than once.'''

# Example of Set

set1 = {123, 345, 3, 4}
set2 = {'Java', 'Python', 'JavaScript'}

print(set1)
print(set2)


# Python Boolean Data Type
'''Python boolean type is one of build-in data types which represents one of the two values either True or False.'''


# Example of Boolean Data Type

a =True
# display the value of a
print(a)

# display tha data type of a
print(type(a))

# Return false as a is not euqal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Return False as a is None
a = None
print(bool(a))

# Return false as a is an empty sequence
a = ()
print(bool(a))

# Return false as a is 0
a = 0.0
print(bool(a))

# Return false as a is 10
a = 10 
print(bool(a))



# Python None Type

'''Python's none type is represented by the "nonetype." It is an object of its own data type. The nonetype represents the null type of values or absence of a value.'''

# Example of None Type

# Declaring a variable 
# And, assigning a Null value (None)

x = None

# Printing its value and type
print("x = ", x)
print("type of x = ", type(x))

# Getting Data Type

print("Getting type of values")

print(type(123))
print(type(9.99))

# Getting type of variables
a = 12
b = 2.33
c = "Kamalesh"
d = (10, 20 ,23)
e = [10, 20, 34]

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))


# Primitive and Non-primitive Data Types

# 1. Primitive Types (complex data structures)
    # * Integers
    # * Floats
    # * Booleans, and
    # * Strings

# 2. Non-primitive Types
    # * Lists
    # * Tuples
    # * Dictionaries, and
    # * Sets
