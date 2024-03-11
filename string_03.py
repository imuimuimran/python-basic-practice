str1 = "Welcome a"


for i in str1:
    print(i)
    
count = 0
for i in str1:
    if i == 'e' or i == 'o' or i == 'a':
        count += 1
print(count)

print(len(str1))