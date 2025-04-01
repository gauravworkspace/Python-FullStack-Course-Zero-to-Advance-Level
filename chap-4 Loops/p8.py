# 20. Find the greatest common divisor (GCD) of two numbers.  
a =int(input("Enter a : "))
b =int(input("Enter b : "))

# GCD 
gcd = 1
for i in range(1,min(a,b)+1):
    if(a%i==0 and b%i==0):
        gcd = i
print(f"The current Greatest Common Divison of {a} and {b} is {gcd}")

