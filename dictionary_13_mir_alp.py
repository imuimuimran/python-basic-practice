input_string = input("Enter a string: ")
input_num = int(input("Enter the starting position (N): "))
input_num_end = int(input("Enter the ending position (N_end): "))

# Creating dictionary for mirror alphabetical operation
alphabets = "abcdefghijklmnopqrstuvwxyz"
reversed_alphabets = alphabets[::-1]  # It is just the reversed order of the alphabets variable
dict1 = dict(zip(alphabets, reversed_alphabets))

# Initialize the result with the unchanged part of the string
result = input_string[:input_num - 1]

# Apply mirror operation to the specified portion of the string
mirror = ""
for i in range(input_num - 1, input_num_end):
    mirror += dict1[input_string[i]]

# Append the mirrored portion to the result
result += mirror

# Append the remaining part of the input string
result += input_string[input_num_end:]

print("The mirror string is:", result)
