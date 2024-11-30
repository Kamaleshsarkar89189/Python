def get_marks(student):
    return student[1]

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student's name:")
    marks = int(input("Enter marks for {name}: "))
    students[name] = marks

for name, marks in sorted(students.items(), key = get_marks, reverse=True):
    print(f"{name} : {marks}")
    
    