# Python - For Loops

# The for loop in Python provides the ability to loop over the items of any sequence, such as a list, tuple or a string. It performs the same action on each item of the sequence. This loop starts with the for keyword, followed by a variable that represents the current item in the sequence. The in keyword links the variable to the sequence you want to iterate over. A colon(:) is  used at the end of the loop header.

# Syntax of Python for loop

# for iterating_var in sequence:
# statement(s)

# Example
    
    # The following example compares each character and displays if it is not a vowel('a','e','i','o','u').

block = '''
The lazy quick brown fox run over the river.
Hi my name is Kamalesh Sarkar, I want to say that you are so lazy.'''

for char in block:
    if char not in "aeiou":
        print(char, end='')
print("\n")

# Python for loop with Tuples

# Example

numbers = (23,4,5,65,7,73,5,6,646,6,)
total = 0
for num in numbers:
    total += num

print("Toatal =", total)

# Python for loop with Lists

# Example 

# Print only those which are divisible by 2.

data = [23,2,4,53,54,4,63,4,34,6]
total1 = 0
for num in data:
    if num%2 == 0:
        print(num)

# Python for Loop with Range Objects

# Python's build-in range() function returns an iterator object that steams a sequence of numbers. This object contains integers from start to stop, separated by the step parameter. You can run a for loop with range as well.

# Syntax

# range(start, stop, step)

# Example

for num in range(5):
    print(num, end='')
print()
for num in range(10,20):
    print(num)

print()
for num in range(1,10,2):
    print(num, end=' ')