# 30. **Write a function to find the sum of all odd numbers in a list.**
# 29. **Write a function to find the sum of all even numbers in a list.**


def Sum_all_Odd(l):
    sum_odd = 0
    sum_even = 0
    for i in l:
        if i%2 !=0:
            sum_odd +=i
        else:
            sum_even += i 
    return sum_odd,sum_even
l = [1,2,3,4,5,6,7,8,9]
print(Sum_all_Odd(l))


