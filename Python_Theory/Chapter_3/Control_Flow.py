# Python - Cntrol Flow
'''
Decision Making Statements

The if Statements

    Python provides if..elif..else control statements as a part of decision making. It consists of three different blocks, which are 
    
    * if block,
    * elif(short of else if) block
    * else block
'''

# Example
marks = 90
result = ""
if marks < 30:
    result = "Failed" # if this is then print 
elif marks > 75: # if the previous is not then print this
    result = "Passed with distrintion"
else: # if the all condition are false then print this
    result = "Passed"
print(result)


# The match Statement

def checkVowel(n):
    match n:
        case 'a': return "Vowel alphabet"
        case 'e': return "Vowel alphabet"
        case 'i': return "Vowel alphabet"
        case 'o': return "Vowel alphabet"
        case 'u': return "Vowel alphabet"
        case _: return "Consonent alphabet"

print (checkVowel('a'))
print (checkVowel('e'))
print (checkVowel('c'))

# n = input("Enter a character: ").lower()
# print(checkVowel(n))

# Loops or Iteration Statements


    # The for Loop
'''The for loop iterates over the items of any sequence, such as a list, tuple or a string'''

# Example

data = ["one", "two", "three"]
for x in data:
    print(x)


# The while Loop
'''The while loop repeatedly executes a target statement as long as a  given boolean expression is true.'''

# Example 

i = 1
while i<6:
    print(i)
    i +=1

# Jump Statements


    # In Python, there are two jump statements break and continue.

    # The break Statement

# Example
y = 0
while y<10:
    print("y: ", y)
    if y == 5:
        print("Breaking..")
        break
    y += 1

print("End")


# The continue Statement

# Example

for letter in "Kamalesh":
    # continue when letter is 'a'
    if letter == "a":
        continue
    print(letter)

