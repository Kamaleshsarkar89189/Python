# Python - OOP Concepts
 
'''
 Class & Object
A class is an user-defined prototype for an object that defines a set of attributes that characterize any object of the class. The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.'''

# Example

# defining class
class Smartphone:
   # constructor    
   def __init__(self, device, brand):
      self.device = device
      self.brand = brand
   
   # method of the class
   def description(self):
      return f"{self.device} of {self.brand} supports Android 14"

# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung")
print(phoneObj.description()) 


