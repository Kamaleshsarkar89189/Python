# Python - Sort Arrays 

'''
Using a sorting algorithm

Using the sort() method from List

Using the built-in sorted() function
'''

# Sort Arrays Using a Sorting Algorithm

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
for i in range(0, len(a)):
   for j in range(i+1, len(a)):
      if(a[i] > a[j]):
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
print (a)

# Sort Arrays Using sort() Method of List

import array as arr

# creating array
orgnlArray = arr.array('i', [10,5,15,4,6,20,9])
print("Original array:", orgnlArray)
# converting to list 
sortedList = orgnlArray.tolist()
# sorting the list
sortedList.sort()

# creating array from sorted list
sortedArray = arr.array('i', sortedList)
print("Array after sorting:",sortedArray)

# Sort Arrays Using sorted() Method

import array as arr
a = arr.array('i', [4, 5, 6, 9, 10, 15, 20])
sorted(a)
print(a)