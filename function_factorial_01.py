def factorial(n):
    ans = 1
    if n == 0:
        ans = 1
    for i in range(1, (n + 1)):
        ans *= i
        
    return ans
    
n = int(input("Enter a number: "))
result = factorial(n)
print("The factorial is:", result)