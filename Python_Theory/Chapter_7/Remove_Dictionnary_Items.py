# Python - Remove Dictionary Items

    # using the del keyword
    # using the pop() method
    # using the popitem() method
    # using the clear() method
    # using dictionary comprehension

# Remove Dictionary Items Using del Keyword

numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
print ("Numbers dictionary before delete operation: \n", numbers)
del numbers[20]
print ("Numbers dictionary before delete operation: \n", numbers)

# Remove Dictionary Items Using pop() Method

val = numbers.pop(30)
print ("nubvers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)

# Remove Dictionary Items Using popitem() Method

val = numbers.popitem()
print ("numbers dictionary after pop operation: \n", numbers)
print ("Value popped: ", val)

# Remove Dictionary Items Using clear() Method
numbers.clear()
print ("numbers dictionary after clear method: \n", numbers)