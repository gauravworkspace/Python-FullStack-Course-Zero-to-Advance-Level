# 23. **Write a function to check if a given year is a leap year.**

def Check_LeapYear(num):
    if num % 400 == 0 or num % 100 != 0 and num % 4 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"

print(Check_LeapYear(2000))