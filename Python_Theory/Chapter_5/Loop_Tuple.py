# Python - Loop Tuples

# Exmaple using for loop

tup = (25, 12, 10, -21, 10, 100)
for num in tup:
   print (num, end = ' ')

print("\n")
# Using while loop

my_tup = (1, 2, 3, 4, 5)
index = 0

while index < len(my_tup):
   print(my_tup[index])
   index += 1

# Tuple methods

'''Sr.No	Methods & Description
    1	
            tuple.count(obj)

            Returns count of how many times obj occurs in tuple

    2	    tuple.index(obj)
            Returns the lowest index in tuple that obj appears  '''

