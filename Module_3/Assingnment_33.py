# Create a class and print using print_info.

class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Occupation: {self.occupation}")

# Example usage
name = input("Enter the name: ")
age = int(input("Enter the age: "))
occupation = input("Enter the occupation: ")

# Create an object of the Person class
person = Person(name, age, occupation)

# Call the print_info method
print("\nPerson Information:")
person.print_info()
