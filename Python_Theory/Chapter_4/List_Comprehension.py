# List Comprehension in Python
'''A list comprehension is a concise way to create lists. It is similar to set builder
 notation in mathematics. It is used to define a list based on an existing iterable object, such as a list, tuple, or string, and apply an expression to each element in the iterable.'''
# Example of Python List Comprehension

string = "hello world"
uppercase_letters = [char.upper() for char in string if char.isalpha()]
print(uppercase_letters)

# List Comprehensions and Lambda

'''In Python, lambda is a keyword used to create anonymous functions. An anonymous function is a function defined without a name.'''

original_list = [1, 2, 3, 4, 5]
doubled_list = [(lambda x: x * 2)(x) for x in original_list]
print(doubled_list)  

# Nested Loops in Python List Comprehension

list1=[1,2,3]
list2=[4,5,6]
CombLst=[(x,y) for x in list1 for y in list2] 
print (CombLst)

# Conditionals in Python List Comprehension

list1=[x for x in range(1,21) if x%2==0]
print (list1)

# List Comprehensions vs For Loop

# Example Using For Loop

chars=[]
for ch in 'TutorialsPoint':
   if ch not in 'aeiou':
      chars.append(ch)
print (chars)


# Example Using List Comprehension

chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
print (chars)


'''Example
The following example uses list comprehension to build a list of squares of numbers between 1 to 10 −'''

squares = [x*x for x in range(1,11)]
print (squares)