def fibonacci(n):
    
    if n == 1: # Base case
        return 0
    elif n == 2: # Base case
        return 1
    else: # Recursion case
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(fibonacci(i))