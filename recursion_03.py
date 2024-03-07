def sum_1_to_N(n):
    # Base case
    if n == 1:
        return 1

    # Recursion case
    ans = n + sum_1_to_N(n -1)
    return ans
    
    

n = int(input("Enter a number: "))
result = sum_1_to_N(n)
print("The sum from 1 to", n, "is:", result)