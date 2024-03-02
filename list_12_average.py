n = int(input("Enter the number of elements in the list: "))

numbers = []

for _ in range(n):
    num = float(input())
    numbers.append(num)
    
total = sum(numbers)
    
average = total / len(numbers)

print("The average of numbers in the list is:", average)