person1 = {}

num_pair = int(input("Enter how the number of key-value pairs: "))

for _ in range(num_pair):
    key = input("Enter Key: ")
    value = input("Enter value: ")
    person1[key] = value
    
print("Person1 information:", person1)

print(person1.keys())
print(person1.values())