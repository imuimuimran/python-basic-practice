def prnt_n_to_1(n):
    # Base case
    if n == 0:
        return

    # Recursion case
    prnt_n_to_1(n -1)
    
    # Print 1 to n
    print(n)
    
    

n = int(input("Enter a number: "))
ans = prnt_n_to_1(n)