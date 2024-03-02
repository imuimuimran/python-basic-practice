start_value = int(input("Enter start value: "))
end_value = int(input("Enter end value: "))

even_sum = 0

for i in range(start_value, end_value):
    if i % 2 == 0:
        even_sum += i
        
print(even_sum)