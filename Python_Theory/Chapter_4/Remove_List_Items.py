# Python - Remove List Items

# Remove List Item Using remove() Method

list1 = ["Rohan", "Physics", 21, 69.75]
print ("Original list: ", list1)

list1.remove("Physics")
print ("List after removing: ", list1)

# Remove List Item Using pop() Method

list2 = [25.50, True, -55, 1+2j]
print ("Original list: ", list2)
list2.pop(2)
print ("List after popping: ", list2)


# Remove List Item Using clear() Method

my_list = [1, 2, 3, 4, 5]

# Clearing the list
my_list.clear()
print("Cleared list:", my_list)


# Remove List Item Using del Keyword

list1 = ["a", "b", "c", "d"]
print ("Original list: ", list1)
del list1[2]
print ("List after deleting: ", list1)