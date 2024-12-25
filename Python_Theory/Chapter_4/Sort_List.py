# Sorting Lists in Python

'''Sorting a list in Python is a way to arrange the elements of the list in either ascending or descending order based'''

# Sorting Lists Using sort() Method

'''Example of Sorting List in Lexicographical Order
'''

list1 = ['physics', 'Biology', 'chemistry', 'maths']
print ("list before sort:", list1)
list1.sort()
print ("list after sort : ", list1)

# Example of Sorting List in Numerical Order

list2 = [10,16, 9, 24, 5]
print ("list before sort", list2)
list2.sort()
print ("list after sort : ", list2)

# Sorting Lists Using sorted() Method

# Syntax
    # sorted(iterable, key=None, reverse=False)

# Example

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# Sorting in descending order
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc) 