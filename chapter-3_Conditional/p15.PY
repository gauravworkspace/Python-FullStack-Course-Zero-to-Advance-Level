# 22. Write a program to check if three given angles form a valid triangle.  

num1 = float(input("Enter angle first : "))
num2 = float(input("Enter angle Second : "))
num3 = float(input("Enter angle Third : "))

#check the valid triangle
if(num1 > 0 and num2 > 0 and num3 > 0 ):
    if(num1 + num2 + num3 == 180 ):
        print("The Trianlge is Valid")
    else:
        print("The Given Angles don't form a valid triangle.")
else:
    print("Angle must be positive values.")