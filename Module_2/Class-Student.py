class Student:
    # Constructor to initialize default values
    def __init__(self, name="Unknown", age=0, grade="Not Assigned"):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to print student information
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Creating three student objects with default and custom values
student1 = Student("Kamalesh", 20, "A")
student2 = Student("Anish", 19, "B")
student3 = Student()  # Using default values

# Printing the information of each student
student1.print_info()
student2.print_info()
student3.print_info()
