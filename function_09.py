def sum_1_to_num(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

num = int(input("Enter a number: "))

result = sum_1_to_num(num)

print("The sum from 1 to", num, "is:", result)
