colors = ("Red", "Blue", "Green", "Yellow", "Orange")

# Traverse normally
print("Travers Result: ")
for color in colors:
    print(color)

print()
# Traverse conditionaly 
print("Travers Result with finding 'r': ")
for color in colors:
    if 'r' in color: # Print the elements which has 'r' 
        print(color)
        
print()
# Traverse conditionaly 
print("Travers Result with finding 'r' or 'l': ")
for color in colors:
    if 'r' in color or 'l' in color: # Print the elements which has 'r' or 'l'
        print(color)
        
print()
# Traverse conditionaly 
print("Travers Result with finding 'O' or 'o': ")
for color in colors:
    if 'o' in color.lower(): # Print the elements which has 'r' or 'l'
        print(color)
        
print()
# Traverse conditionaly 
print("Travers Result with finding 'R' or 'r': ")
for color in colors:
    if 'R' in color.upper(): # Print the elements which has 'r' or 'l'
        print(color)