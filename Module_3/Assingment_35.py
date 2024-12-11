# Demostrate Polymorphism

# Base class
class Animal:
    def sound(self):
        return "Some generic animal sound"

# Derived class 1
class Dog(Animal):
    def sound(self):
        return "Bark"

# Derived class 2
class Cat(Animal):
    def sound(self):
        return "Meow"

# Derived class 3
class Cow(Animal):
    def sound(self):
        return "Moo"

# Function to demonstrate polymorphism
def animal_sound(animal):
    print(f"{animal.__class__.__name__} makes the sound: {animal.sound()}")

# Example usage
animals = [Dog(), Cat(), Cow(), Animal()]

for animal in animals:
    animal_sound(animal)
