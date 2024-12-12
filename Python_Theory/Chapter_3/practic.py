# my_dict = {"name": "Kamalesh", "age": 5}
# key = "name"
# if key in my_dict:
#     print(f"Key '{key}' exists in the dictionary.")
# else:
#     print(f"Key '{key}' does not exist in the dictionary.")

# import math
# print(math.sqrt(16))

# import random
# random_number = random.randint(1, 10) # Random integer between 1 and 10
# print(random_number)


# try:
#     with open("file.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     print("Execution complete.")


# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#     def details(self):
#         return f"Title: {self.title}, Author: {self.author}"
# b = Book("Python", "Author")
# print(b.details())

rows=3
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i + 1):
        print(j, end="")
    print()
print("\n")
rows = 4
alphabet = ['A', 'B', 'C', 'D']
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    print((alphabet[i - 1] + " ") * i)

print("\n")
n = 3
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    numbers = str(i) * (2 * i - 1)
    print(spaces + numbers)

print("\n")
rows = 5
cols = 7
for i in range(rows):
    if i == 0 or i == rows - 1:
        print('*' * cols)
    else:
        print('' + ' ' * (cols - 2) + '')