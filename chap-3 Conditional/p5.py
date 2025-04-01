# Write a program to determine the grade of a student based on marks (A, B, C, etc.).



marks = int(input("Enter Marks : "))



# check the Grade of student
if marks >= 85 and marks <100:
    print("Grade A")
elif marks >=70 and marks < 85:
    print("Grade B")
elif marks >=55 and marks < 70:
    print("Grade C")
elif marks >= 33 and marks < 55:
    print("Grade D")
else:
    print("Fail")