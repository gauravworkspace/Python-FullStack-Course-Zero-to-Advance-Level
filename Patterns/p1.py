# 21. Print a square pattern of stars `(*)`.  
"""
* * * * 
* * * * 
* * * * 
* * * *
"""
num = int(input("Enter your number "))

for i in range(1,num+1):
    for j in range(1,num+1):
        print("*",end=" ")
    print()

print("Right Angle Triangle")
# 22. Print a right-angled triangle pattern of stars.  
"""
*
* *
* * *
"""

# num = 4
for i in range(1,num+1):
    for i in range(1,i+1):
        print("*",end=" ")
    print()