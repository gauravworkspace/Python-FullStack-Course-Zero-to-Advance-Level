# 23. Write a program to determine if a year is a century year and a leap year.  

year = int(input("Enter the year : "))

if year % 100 == 0:
    print(f"{year} is the century year")

    # check if it's also a leap year
    if(year % 400 == 0 ):
        print(f"{year} is also a leap year")
    else:
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a century year")

    # check if it's  leap year (non-century)
    if(year%4==0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
