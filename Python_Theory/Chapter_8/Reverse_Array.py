# Python - Reverse Arrays

# Ways to Reverse an Array in Python

'''
Using slicing operation
Using reverse() method
Using reversed() method
Using for loop
'''

# Using slicing operation

import array as arr

# creating array
numericArray = arr.array('i', [88, 99, 77, 55, 66])

print("Original array:", numericArray)
revArray = numericArray[::-1]
print("Reversed array:",revArray)

# Reverse an Array Using reverse() Method

import array as arr

# creating an array
numericArray = arr.array('i', [10,5,15,4,6,20,9])
print("Array before reversing:", numericArray)

# converting the array into list
newArray = numericArray.tolist()

# reversing the list
newArray.reverse()

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)

# Reverse an Array Using reversed() Method

import array as arr

# creating an array
numericArray = arr.array('i', [12, 10, 14, 16, 20, 18])
print("Array before reversing:", numericArray)

# reversing the array
newArray = list(reversed(numericArray))

# creating a new array from reversed list
revArray = arr.array('i', newArray)
print ("Array after reversing:",revArray)

# Using for Loop

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i')
for i in range(len(a)-1, -1, -1):
   b.append(a[i])
print(a)
print(b)