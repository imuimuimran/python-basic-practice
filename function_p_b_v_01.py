def add_one(x):
    x = x +1
    print("The inner function result is:", x)
    
x = 5
add_one(x)
print("The outer function result is:", x)