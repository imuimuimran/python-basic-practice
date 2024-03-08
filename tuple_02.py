colors = ("Red", "Blue", "Green", "Yellow", "Orange")

print(type(colors))
print(colors)
print(len(colors))

colors1 = ("Red") # Treat as string
colors2 = ("Red",) # Treat as tuple for putting coma
colors3 = tuple(("Red")) # Treat as tuple but print seperately like : ('R', 'e', 'd')
colors4 = tuple(("Red",)) # Treat as tuple and print as single item for putting coma

print(type(colors1))
print(type(colors2))
print(type(colors3))
print(type(colors4))

print(colors1)
print(colors2)
print(colors3)
print(colors4)