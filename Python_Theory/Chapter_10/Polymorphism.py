# Polymorphism

# Polymorphism is a Greek word meaning having multiple forms. In OOP, polymorphism occurs when each sub class provides its own implementation of an abstract method in base class.

# Types of Polymorphism

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(1, 2, 3))  # Outputs: 6
print(calc.add(1, 2))     # Outputs: 3


# Run-Time Polymorphism (Dynamic Binding):

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
# Outputs:
# Bark
# Meow
