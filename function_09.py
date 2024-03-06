def sum_1_to_num(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

num1 = int(input("Enter a number: "))
result1 = sum_1_to_num(num1)
print("The sum from 1 to", num1, "is:", result1)

num2 = int(input("Enter a number: "))
result2 = sum_1_to_num(num2)
print("The sum from 1 to", num2, "is:", result2)
