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


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def details(self):
        return f"Title: {self.title}, Author: {self.author}"
b = Book("Python", "Author")
print(b.details())