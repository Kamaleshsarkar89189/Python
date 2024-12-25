# Python - Access List Items

# Accessing List Items with Indexing
print("Accessing List Items with Indexing\n")
list1 = ["Rohan", "Physics", 21, 69.75]
list2 = [1, 2, 3, 4, 5]

print ("Item at 0th index in list1: ", list1[0])
print ("Item at index 2 in list2: ", list2[2])

print("\n")
# Access List Items with Negative Indexing

print("Access List Items with Negative Indexing\n")
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Item at 0th index in list1: ", list1[-1])
print ("Item at index 2 in list2: ", list2[-3])

print("\n")

# Access List Items with Slice Operator

print("Access List Items with Slice Operator\n")
    # Syntax: 
        # [start:stop] 

list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]
list3 = ["Rohan", "Physics", 21, 69.75]

print ("Items from index 1 to last in list1: ", list1[1:])
print ("Items from index 0 to 1 in list2: ", list2[:2])
print ("Items from index 0 to index last in list3", list3[:])

print("\n")
# Access Sub List from a List
print("Access Sub List from a List\n")
list1 = ["a", "b", "c", "d"]
list2 = [25.50, True, -55, 1+2j]

print ("Items from index 1 to 2 in list1: ", list1[1:3])
print ("Items from index 0 to 1 in list2: ", list2[0:2])