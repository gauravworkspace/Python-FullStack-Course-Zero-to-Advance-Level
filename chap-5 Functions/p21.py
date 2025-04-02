# 21. **Write a function to generate a multiplication table for a number.**

def Table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

Table(5)


# 22. **Write a function to count the number of vowels in a string.**

def Count(string):
    vowels = "aieouAIEOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1
    return count

print(Count("Gaurav"))