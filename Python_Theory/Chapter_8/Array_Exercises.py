# Python - Array Exercises

# Python program to find the largest number in an array −

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)

# Python program to store all even numbers from an array in another array −

import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
b = arr.array('i')
for i in range(len(a)):
   if a[i]%2 == 0:
      b.append(a[i])
print ("Even numbers:", b)