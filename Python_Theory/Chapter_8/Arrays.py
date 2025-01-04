# Python - Arrays

# Arrays in Python

'''Unlike other programming languages like C++ or Java, Python does not have built-in support for arrays. However, Python has several data types like lists and tuples (especially lists) that are often used as arrays but, items stored in these types of sequences need not be of the same type.'''

# Example

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# creating an array with char type
a = arr.array('u', 'BAT')
print (type(a), a)

# creating an array with float type
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)

# Python array type is decided by a single character Typecode argument. 

'''typecode	    Python data type	Byte size
    'b'	         signed integer	    1
    'B'	         unsigned integer	1
    'u'	         Unicode character	2
    'h'	         signed integer	    2
    'H'	         unsigned integer	2
    'i'	         signed integer	    2
    'I'	         unsigned integer	2
    'l'	         signed integer	    4
    'L'	         unsigned integer	4
    'q'	         signed integer	    8
    'Q'	         unsigned integer	8
    'f'	         floating point	    4
    'd'	         floating point	    8'''

# Basic Operations on Python Arrays

'''
    Traverse − Print all the array elements one by one.

    Insertion − Adds an element at the given index.

    Deletion − Deletes an element at the given index.

    Search − Searches an element using the given index or by the value.

    Update − Updates an element at the given index.
'''

# Accessing Array Element

from array import *
array1 = array('i', [10,20,30,40,50])
print (array1[0])
print (array1[2])

# Insertion Operation

from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(1,60)
for x in array1:
    print(x)

# Search Operation

from array import *
array1 = array('i', [10,20,30,40,50])
print (array1.index(40))

# Update Operation

from array import *
array1 = array('i', [10,20,30,40,50])
array1[2] = 80
for x in array1:
   print(x)

# Copy Arrays Using Assignment Operator

import array as arr
a = arr.array('i', [110, 220, 330, 440, 550])
b = a
print("Copied array:",b)
print (id(a), id(b))

# Copy Arrays Using Deep Copy

import array as arr
import copy
a = arr.array('i', [110, 220, 330, 440, 550])
b = copy.deepcopy(a)
print("Copied array:",b)