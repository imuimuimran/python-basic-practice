def calculate_average():
    n = int(input("Enter the number of elements of list: "))
    
    numbers = []
    
    for _ in range(n):
        num = float(input())
        numbers.append(num)
        
    total = sum(numbers)
        
    average = total / len(numbers)
    
    return average

result = calculate_average()

print("The average of numbers in the list is:", result)