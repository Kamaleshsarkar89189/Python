# Python - Class Methods

# Creating Class Methods in Python

'''Using classmethod() Function
Using @classmethod Decorator
'''

# Using classmethod() Function


'''
Using @classmethod Decorator
Use of @classmethod() decorator is the prescribed way to define a class method as it is more convenient than first declaring an instance method and then transforming it into a class method.
'''

# Instead of self (used in instance methods), cls is passed as the first argument to a class method. 

class Vehicle:
    type = "Car"

    @classmethod
    def set_type(cls, new_type):
        cls.type = new_type

    @classmethod
    def get_type(cls):
        return cls.type

print(Vehicle.get_type())  # Outputs: Car
Vehicle.set_type("Truck")
print(Vehicle.get_type())  # Outputs: Truck
