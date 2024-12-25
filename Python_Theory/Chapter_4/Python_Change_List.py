# Python - Change List Items

'''List is a mutable data type in Python. It means, the contents of list can be modified in place, after the object is stored in the memory.'''

list3 = [1, 2, 3, 4, 5]
print ("Original list ", list3)
list3[2] = 10
print ("List after changing value at index 2: ", list3)

# Change Consecutive List Item
print("Change Consecutive List Item")
list1 = ["a", "b", "c", "d"]

print ("Original list: ", list1)

list2 = ['Y', 'Z']
list1[1:3] = list2

print ("List after changing with sublist: ", list1)

print("\n")

# Change a Range of List Items

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
list2 = ['X','Y', 'Z']
list1[1:3] = list2
print ("List after changing with sublist: ", list1)