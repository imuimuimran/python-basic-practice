def pow_of_num(x, y):
    # Base case
    if y == 0:
        return 1

    # Recursion case
    ans = x * pow_of_num(x, y-1)
    return ans
    
    

x = int(input("Enter a number: "))
y = int(input("Enter a power of the number: "))
result = pow_of_num(x, y)
print("The result of", x, "power", y, "is:", result)