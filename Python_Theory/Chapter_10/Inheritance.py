# Inheritance
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (referred to as a child class or subclass) to inherit properties and behaviors (fields and methods) from another class (called the parent class or superclass). 

# Example

class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Car(Vehicle):
    def honk(self):
        print("Honking car horn...")

my_car = Car()
my_car.start()  # Inherited method
my_car.honk()   # Method from Car class

# Multiple Inheritance:

class Engine:
    def start_engine(self):
        print("Engine started.")

class Wheels:
    def rotate_wheels(self):
        print("Wheels are rotating.")

class Car(Engine, Wheels):
    pass

my_car = Car()
my_car.start_engine()
my_car.rotate_wheels()


# Hierarchical Inheritance:

class Animal:
    def breathe(self):
        print("Breathing...")

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Cat(Animal):
    def meow(self):
        print("Meowing...")

# Multilevel Inheritance:

class Animal:
    def eat(self):
        print("Eating...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Human(Mammal):
    def speak(self):
        print("Speaking...")

# Accessing Parent Class Methods:

class Animal:
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def sound(self):
        super().sound()  # Calls the parent class method
        print("Bark")

my_dog = Dog()
my_dog.sound()
