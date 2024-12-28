# Python - Dictionaries

'''In Python, a dictionary is a built-in data type that stores data in key-value pairs. It is an unordered, mutable, and indexed collection. Each key in a dictionary is unique and maps to a value.'''

# Creating a Dictionary

# Creating a dictionary using curly braces
sports_player = {
   "Name": "Sachin Tendulkar",
   "Age": 48,
   "Sport": "Cricket"
}
print ("Dictionary using curly braces:", sports_player)
# Creating a dictionary using the dict() function
student_info = dict(name="Alice", age=21, major="Computer Science")
print("Dictionary using dict():",student_info)  

# Accessing Dictionary Items
student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Accessing values using square brackets
name = student_info["name"]
print("Name:",name)  

# Accessing values using the get() method
age = student_info.get("age")
print("Age:",age)  


# Modifying Dictionary Items

student_info = {
   "name": "Alice",
   "age": 21,
   "major": "Computer Science"
}
# Modifying an existing key-value pair
student_info["age"] = 22

# Adding a new key-value pair
student_info["graduation_year"] = 2023
print("The modified dictionary is:",student_info)

# Removing Dictionary Items

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Removing an item using the del statement
del student_info["major"]

# Removing an item using the pop() method
graduation_year = student_info.pop("graduation_year")

print(student_info) 

# Iterating Through a Dictionary

student_info = {
   "name": "Alice",
   "age": 22,
   "major": "Computer Science",
   "graduation_year": 2023
}
# Iterating through keys
for key in student_info:
   print("Keys:",key, student_info[key])

# Iterating through values
for value in student_info.values():
   print("Values:",value)

# Iterating through key-value pairs
for key, value in student_info.items():
   print("Key:Value:",key, value) 