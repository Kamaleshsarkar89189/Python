# Python - Join Lists

# Join Lists Using Concatenation Operator

# Two lists to be joined
L1 = [10,20,30,40]
L2 = ['one', 'two', 'three', 'four']
# Joining the lists
joined_list = L1 + L2

# Printing the joined list
print("Joined List:", joined_list)

# Join Lists Using List Comprehension

# Two lists to be joined
L1 = [36, 24, 3]
L2 = [84, 5, 81]
# Joining the lists using list comprehension
joined_list = [item for sublist in [L1, L2] for item in sublist]
# Printing the joined list
print("Joined List:", joined_list)
