# Write a program to swap two numbers without using a third variable.

n1 = 5
n2 = 3

# Original number before swapping 
print("Before Swapping : " ,"n1 is ", n1,  " and  n2 is ", n2 )

n1 = n1 + n2 
n2 = n1 - n2
n1 = n1 - n2
# n1 , n2 = n2 , n1  # Very short method to swap in linear way
# After swapping 
print("After Swapping : ","n1 is ", n1 , "and  n2 is ",n2)