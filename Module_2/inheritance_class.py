# Base class
class Student:
    # Constructor for the Student class
    def __init__(self, name="Unknown", age=0, grade="Not Assigned"):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to print student information
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Derived class
class CSEStudent(Student):
    # Constructor for the CSEStudent class
    def __init__(self, name="Unknown", age=0, grade="Not Assigned", graduation_year="Unknown"):
        super().__init__(name, age, grade)  # Call to the base class constructor
        self.graduation_year = graduation_year

    # Overriding the print_info method
    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Graduation Year: {self.graduation_year}")
 
# Creating objects
student1 = Student("Alice", 20, "A")
cse_student1 = CSEStudent("Bob", 21, "A+", 2024)

# Printing information
print("Base class Student:")
student1.print_info()

print("\nDerived class CSEStudent:")
cse_student1.print_info()
