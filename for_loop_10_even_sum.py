odd_sum = 0
even_sum = 0

for i in range(1,101):
    if i % 2 == 1: # This line extract only odd numbers in range
        odd_sum += i
    if i % 2 == 0: # # This line extract only even numbers in range
        even_sum += i
        
print(odd_sum)
print(even_sum)


