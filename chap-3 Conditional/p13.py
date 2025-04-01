# 20. Write a program to determine a person’s Body Mass Index (BMI) category.  

weight = float(input("Enter Your weight : "))
height = float(input("Enter Your height : "))

# calculate the bmi
bmi = weight/height**2

# check the bmi 
if bmi <18.5:
    category = "Underweight"
elif 18.5 <=bmi<25:
    category = "Normal Weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display the BMI and Category
print(f"Your BMI is : {bmi:.2f}")
print(f"Category:{category}")   