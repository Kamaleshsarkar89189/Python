input_string = input("Enter a string: ")

occurances ={}

for char in input_string.lower():
    if char.isalpha():
        occurances[char]  = occurances.get(char, 0) + 1

print(occurances)
