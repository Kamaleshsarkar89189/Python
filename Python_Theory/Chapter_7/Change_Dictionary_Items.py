# Python - Change Dictionary Items

# Initial dictionary
person = {'name': 'Kamalesh', 'age': 21, 'city': 'Kolkata'}
# Modifying the value associated with the key 'age'
person['age'] = 22
print(person)

# Updating Multiple Dictionary Values

person.update({'age': 35, 'city': 'Delhi'})
print(person)

# Modify Dictionary by Adding New Key-Value Pairs

# Example: Using Assignment Operator

# Initial dictionary
person = {'name': 'Alice', 'age': 25}
# Adding a new key-value pair 'city': 'New York'
person['city'] = 'New York'
print(person)

# Example: Using the setdefault() Method

# Initial dictionary
person = {'name': 'Alice', 'age': 25}
# Adding a new key-value pair 'city': 'New York'
person.setdefault('city', 'New York')
print(person)

# Modify Dictionary by Removing Key-Value Pairs

# Example: Using the del Statement

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
del person['age']
print(person)

# Example: Using the pop() Method

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the key-value pair associated with the key 'age'
removed_age = person.pop('age')

print(person)
print("Removed age:", removed_age)

# Example: Using the popitem() Method

# Initial dictionary
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# Removing the last key-value pair 
removed_item = person.popitem()

print(person)
print("Removed item:", removed_item)