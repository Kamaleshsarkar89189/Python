# Python - Sets

'''In Python, a set is an unordered collection of unique elements. Unlike lists or tuples, sets do not allow duplicate values i.e. each element in a set must be unique. Sets are mutable, meaning you can add or remove items after a set has been created.'''

# Creating a Set in Python

my_set = {1, 2, 3, 4, 5}
print (my_set)

# Duplicate Elements in Set

my_set = {1, 2, 2, 3, 3, 4, 5, 5} 
print (my_set)

# Sets can contain elements of different data types, including numbers, strings, and even other sets (as long as they are immutable) −

mixed_set = {1, 'hello', (1, 2, 3)}
print (mixed_set)

# Adding Elements in a Set
my_set = {1, 2, 3, 3}
# Adding an element 4 to the set
my_set.add(4)  
print (my_set)

# Removing Elements from a Set

my_set = {1, 2, 3, 4}
# Removes the element 3 from the set
my_set.remove(3)  
print (my_set)

# Alternatively, you can use the discard() function to remove an element from the set if it is present. Unlike remove(), discard() does not raise an error if the element is not found in the set −

my_set = {1, 2, 3, 4}
# No error even if 5 is not in the set
my_set.discard(5)  
print (my_set)

# Membership Testing in a Set

my_set = {1, 2, 3, 4}
if 2 in my_set:
   print("2 is present in the set")
else:
   print("2 is not present in the set")