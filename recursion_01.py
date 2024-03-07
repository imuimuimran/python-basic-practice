def prnt_n_to_1(n):
    # Base case
    if n == 0:
        return
    
    # Print n to 1
    print(n)
    # Recursion case
    prnt_n_to_1(n -1)
    
    

n = int(input("Enter a number: "))
ans = prnt_n_to_1(n)