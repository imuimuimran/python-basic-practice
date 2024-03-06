def sum_of_numbers(*args):
    sum = 0
    for i in args:
        sum += i
        
    return sum

# Arbitary Argument
result = sum_of_numbers(5, 12, 3, 10)

print("The sum of args is:", result)