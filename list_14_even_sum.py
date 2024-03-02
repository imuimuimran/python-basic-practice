def claculate_even_sum(numbers):
    even_sum = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            
    return even_sum

numbers = [1,2,3,4,5,6,7,8,9,10]

result = claculate_even_sum(numbers)

print(result)
        
    