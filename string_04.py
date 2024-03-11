str1 = "I love my country Bangladesh"

# find vowel in string
count = 0
for i in str1:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        count += 1
print("Total vovel in", "'",str1,"'", "is:", count)

print("The length of", "'",str1,"'", "is:", len(str1))