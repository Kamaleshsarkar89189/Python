# Python - Access Tuple Items

# Exmaple
tuple1 = ("Kamalesh", "Physics", 21, 69.75)
tuple2 = (1, 2, 3, 4, 5)

print ("Item at 0th index in tuple1: ", tuple1[0])
print ("Item at index 2 in tuple2: ", tuple2[2])

# Access Tuple Items with Slice Operator

# [start:stop] 
# Where, start is the starting index.
        # stop is the ending index.

tuple1 = ("a", "b", "c", "d")
tuple2 = (25.50, True, -55, 1+2j)
tuple3 = (1, 2, 3, 4, 5)
tuple4 = ("Rohan", "Physics", 21, 69.75)

print ("Items from index 1 to last in tuple1: ", tuple1[1:])
print ("Items from index 0 to 1 in tuple2: ", tuple2[:2])
print ("Items from index 0 to index last in tuple3", tuple3[:])