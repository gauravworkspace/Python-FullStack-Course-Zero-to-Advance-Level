# 5. **Write a function to calculate the sum of all numbers in a list.**

def Sum_List(numbers):
    # total_sum = 0
    # for num in numbers:
    #     total_sum += num
    # return total_sum
    total_sum = sum(numbers)
    return total_sum
print(Sum_List([1,2,3,4,5]))