input_string = input("Enter a string: ")


# Creating dictionary for mirror alphabetical operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reversed_alphabets = alphabets[::-1] # It is just the reversed order of the alphabets variable
dict1 = dict(zip(alphabets, reversed_alphabets))

# finding the mirror string
mirror = ""
for i in range(0, len(input_string)):
    mirror = mirror + dict1[input_string[i]]

print("The mirror string is:", mirror)
