# Write a Python program to check whether a given year is a leap year or not.

year = int(input("Enter Your Year : "))

# Logic to calculate the leap year
if(year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("The Given Year is Leap Year")
else:
    print("The Given Year is not Leap Year")
    