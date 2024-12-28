# Python - Set Operators

'''The set operators in Python are special symbols and functions that allow you to perform various operations on sets, such as union, intersection, difference, and symmetric difference. '''

# Python Set Union Operator (|)
'''The union of two sets is a set containing all distinct elements that are in A or in B or both. For example,
'''

# Example
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 45, 73}
union_set1 = set1.union(set2)
union_set2 = set3 | set4
print ('The union of set1 and set2 is', union_set1)
print ('The union of set3 and set4 is', union_set2)

# Python Set Intersection Operator (&)
'''The intersection of two sets AA and BB, denoted by A∩B, consists of all elements that are common to both in A and B. For example,
'''

# Python provides the intersection() function or the & operator to perform this operation. The resulting set contains only the elements present in both sets −

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
intersection_set1 = set1.intersection(set2)  
intersection_set2 = set3  & set4
print ('The intersection of set1 and set2 is', intersection_set1)
print ('The intersection of set3 and set4 is', intersection_set2)

# Python Set Difference Operator (-)

'''The difference (subtraction) between two sets consists of elements present in the first set but not in the second set. It is defined as follows. The set A−B consists of elements that are in A but not in B. For example,

'''

# Python provides the difference() function or the - operator to perform this operation. The resulting set contains elements unique to the first set −

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
difference_set1 = set1.difference(set2)
difference_set2 = set3 - set4
print ('The difference between set1 and set2 is', difference_set1)
print ('The difference between set3 and set4 is', difference_set2)

# Python Set Symmetric Difference Operator

# A Δ B = (A − B) ⋃ (B − A)

'''Python provides the symmetric_difference() function or the ^ operator to perform this operation. The resulting set contains elements that are unique to each set.'''

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = {6, 8, 9}
set4 = {9, 8, 73}
symmetric_difference_set1 = set1.symmetric_difference(set2)  
symmetric_difference_set2 = set3 ^ set4
print ('The symmetric difference of set1 and set2 is', symmetric_difference_set1)
print ('The symmetric difference of set3 and set4 is', symmetric_difference_set2)

# Python Subset Testing Operation

'''You can check whether one set is a subset of another using the issubset() function or the <= operator. A set A is considered a subset of another set B if all elements of A are also present in B −'''

set1 = {1, 2}
set2 = {1, 2, 3, 4}
set3 = {64, 47, 245, 48}
set4 = {64, 47, 3}
is_subset1 = set1.issubset(set2)  
is_subset2 = set3 <= set4
print ('set1 is a subset of set2:', is_subset1)
print ('set3 is a subset of set4:', is_subset2)

