# 20. **Write a function to check if a number is a perfect square.**

def Perfect_Square(num):
     square_root = num ** 0.5 
     return square_root.is_integer()
print(Perfect_Square(25))