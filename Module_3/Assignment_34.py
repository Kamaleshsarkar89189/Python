# Determine inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("This animal makes a sound.")

# Derived class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def sound(self):
        print("The dog barks.")

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

# Derived class
class Cat(Animal):
    def sound(self):
        print("The cat meows.")

# Example usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print("Dog Info:")
dog.print_info()
dog.sound()

print("\nCat Info:")
cat.sound()
