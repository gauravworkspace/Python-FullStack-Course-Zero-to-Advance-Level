# 26. **Write a function to find the least common multiple (LCM) of two numbers.**

import math

def LCM(a,b):
    lcm = abs(a*b)//math.gcd(a,b)
    return lcm

print(LCM(2,4))



# 25. **Write a function to find the greatest common divisor (GCD) of two numbers.**

def GCD(a,b):
    GCD = math.gcd(a,b)
    return GCD
print(GCD(24,36))