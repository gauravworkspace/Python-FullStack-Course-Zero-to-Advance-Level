# OOPS in Python
# OOP - object oriented Programming 
# student

student_1 = ['Madhav',10]
student_2 = ['Vishakha',12]

# print(f"{student_1[0]}  is in class  {student_1[1]}")
# print(f"{student_2[0]}  is in class  {student_2[1]}")



# Using OOPS- Creating Student records

class Student: 
    def __init__(self,name,grade,percentage): # __init__ method -Constructor value initalize 
        self.name = name
        self.grade =grade
        self.percentage= percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade} with {self.percentage} percent.")
# Object - instance of class
student1 = Student('Madhav',11,98)
# print(student1)
print(student1.name, student1.grade)

student2 = Student('Gaurav',12,78)
print(student2.name,student2.grade)

student1.student_details()

print(student1.__dict__)


# modify object property 
print(student1.percentage)
student1.percentage = 8
print(student1.percentage)

# delete object
del student1
print(student1)

