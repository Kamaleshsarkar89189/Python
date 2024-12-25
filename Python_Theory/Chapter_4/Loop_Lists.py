# Python - Loop Lists

lst = [25, 12, 10, -21, 10, 100]
for num in lst:
   print (num, end = ' ')

# List Items with While Loop

my_list = [1, 2, 3, 4, 5]
index = 0

while index < len(my_list):
   print(my_list[index])
   index += 1

#    Iterate using List Comprehension

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print (squared_numbers)

# Iterate using the enumerate() Function

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
   print(index, fruit)