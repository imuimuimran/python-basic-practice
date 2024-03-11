input_string = input("Enter a string: ")
input_num = int(input("Enter the N: "))

# Creating dictionary for mirror alphabetical operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reversed_alphabets = alphabets[::-1] # It is just the reversed order of the alphabets variable
dict1 = dict(zip(alphabets, reversed_alphabets))

# finding the part of alphabetical string where the morror operation will be done
prefix = input_string[0:input_num-1]
suffix = input_string[input_num-1:]

# finding the mirror string
mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]

# Create the final string

result = prefix + mirror
print("The mirror string is:", result)  