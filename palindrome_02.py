str = input("enter string: ")

clean_str = (str.replace(" ", "")).lower()
print(clean_str)

reverse_str = clean_str[::-1]
print(reverse_str)

if reverse_str == clean_str:
    print(reverse_str, "is a palindrome")
else:
    print(reverse_str, "is not a palindrome")