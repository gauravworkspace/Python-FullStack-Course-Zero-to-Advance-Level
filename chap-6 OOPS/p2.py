# Abstraction - Hiding unecessary details from users through class, methods

class Student: # student name
    def __init__(self,name,grade,percentage):
        self.name = name #attribute
        self.grade = grade
        self.percentage = percentage

    def student_details(self): # method
        print(f"{self.name} is in class {self.grade},with {self.percentage}% ")

# Object - instance of class
student1 = Student('Madhav',11,98)
student2 = Student('Vishakha',12,99)

# print(student1.percentage)
student1.student_details()