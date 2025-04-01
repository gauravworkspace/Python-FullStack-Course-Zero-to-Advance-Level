# 18. Check whether a given number is an Armstrong number.  

number = 153
original_number = number
sum_of_nums = 0 

length_string=len(str(number))

while number >0:
    digit = number % 10
    sum_of_nums += (digit**length_string)
    number //=10

if(original_number == sum_of_nums):
    print("Armstrong number")
else:
    print("Not Armstrong number")