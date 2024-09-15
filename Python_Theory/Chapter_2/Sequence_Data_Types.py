# Python Sequence Data Types
'''
    * List Data Type
    * Tuple Data Type
    * Range Data Type
'''

# Python List Data Type

list = [ 'acbd', 578, 3.56, 'Kamalesh', 79.3]
shortlist = [123, 'Kama']

print(list)     # Prints complex list
print(list[0])     # Prints first element of the list
print(list[1:3])    # Prints elements from starting from 2nd till 3rd
print(list[2:])     # Prints elements starting from 3rd element
print(shortlist * 2)    # Print list two times
print(list + shortlist) # Print concatenated lists


# Python Tuple Data Type

'''Python tuple is another sequence data type that is similar to a list. A Python tuple consists of a number of values separated by commas.'''

# Example of Tuple Data Type

tuple = ('abcd', 3.23, 344, 'Kamalesh', 34.44)
tinytuple = (123, 'Kamalesh')

print(tuple)             # Print the complete tuple
print(tuple[0])          # Print first element of the tuple
print(tuple[1:3])        # Print elements of the tuple strating from 2nd till 3rd
print(tuple[2:])         # Print elements of the tuple starting from 3rd element
print(tinytuple * 2)     # Print the contents of the tuple twice
print(tuple + tinytuple) # Print concatenated tuples


# Python Range Data Type
'''A Python range is an immutable sequence of number which is typically used to iterate through a specific number of items.

    range(start, stop, step)
    
    * start: Integer number to specify starting position, (Its optional, Default: 0)
    
    * stop: Integer number to specify ending position (It's mandatory) 

    * step: Integer number to specify increment, (Its optional, Default: 1)
    
    '''

# Example of Range Data Type

for i in range(5):
    print(i)

print("Print the number starting from 2 instead of 0")
# Print the number staring from 2 instead of 0 -

for i in range(2,5):
    print(i)

print("Print the number starting from 1 but with an increment of 2 instead of 1:")

for i in range(1,5,2):
    print(i)

    