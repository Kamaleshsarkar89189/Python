# Python - Access Dictionary Items
'''Using square brackets []
The get() method
Iterating through the dictionary using loops
Or specific methods like keys(), values(), and items()'''

# Access Dictionary Items Using Square Brackets []



Students = {"Kamalesh Sarkar": "North Dinajput", "Kisan":"East Dinajpur",}

print ("District of Kamalesh is : ", Students['Kamalesh Sarkar'])
print ("District of Kisan is : ", Students['Kisan'])


# Access Dictionary Items Using get() Method

print ("District of Kamalesh is: ", Students.get('Kamalesh Sarkar'))
print ("District of Kisan is: ", Students.get('Kisan'))

# Access Dictionary Keys

all_keys = Students.keys()
print("Keys:", all_keys)