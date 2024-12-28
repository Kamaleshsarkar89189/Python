# Python - Copy Sets

# Copy Sets Using the copy() Method

# Original set
original_set = {1, 2, 3, 4, 5}

# Using the copy() method to copy the set
copied_set = original_set.copy()

# Displaying the original and copied sets
print("Original Set:", original_set)
print("Copied Set:", copied_set)


# Copy Sets Using the set() Function

# Original set
original_set = {1, 2, 3, 4}
# Copying the set using the set() function
copied_set = set(original_set)
print("copied set:", copied_set) 

# Demonstrating that the sets are independent
copied_set.add(5)
print("copied set:",copied_set)      
print("original set:",original_set)   

# Copy Sets Using Set Comprehension

# Original set
original_set = {1, 2, 3, 4, 5}

# Copying the set using set comprehension
copied_set = {x for x in original_set}
print("Copied set:", copied_set)