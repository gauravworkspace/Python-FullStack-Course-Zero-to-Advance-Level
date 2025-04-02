# 6. **Write a function to find the average of a list of numbers.**

def Average_calculate(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    
    num_digit = len(numbers)
    average= total_sum/num_digit
    return average
# Call the function
result = Average_calculate([1,2,3,4,5,6])
print(result)
