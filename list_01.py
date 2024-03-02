fruits = ["Apple", "Banana", "Mango"]

print(type(list))
print(fruits[1])
for fruit in fruits:
    print(fruit)

print("Total item of list is:", len(fruits))

if "Banan" in fruits:
    print("Banana is in fruits")
else:
    print("There is no such item in the list")