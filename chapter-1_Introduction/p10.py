# Write a program to calculate the sum of the first N natural numbers.

number = int(input("Enter the number = "))
# Calculate the sum of n natural number
total_sum = 0
for i in range(1,number+1):

        total_sum += i

# Display result
print(f"Sum of first {number} natural number is : {total_sum}")

    