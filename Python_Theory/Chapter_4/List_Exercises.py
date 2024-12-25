# Python program to find unique numbers in a given list.

L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
L2 = []
for x in L1:
   if x not in L2:
      L2.append(x)
print (L2)


# Python program to find sum of all numbers in a list.

L1 = [1, 9, 1, 6, 3, 4]
ttl = 0
for x in L1:
   ttl+=x
print ("Sum of all numbers Using loop:", ttl)
ttl = sum(L1)
print ("Sum of all numbers sum() function:", ttl)


# Python program to create a list of 5 random integers.

import random
L1 = []
for i in range(5):
   x = random.randint(0, 100)
   L1.append(x)
print (L1)