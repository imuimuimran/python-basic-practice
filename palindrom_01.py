def check_palindrome(str):
    # clean the string
    clean_str = (str.replace(" ", "")).lower()
    print(clean_str)
    
    reverse_str = clean_str[::-1]
    print(reverse_str)
    return reverse_str == clean_str

str = input("enter string: ")

if check_palindrome(str):
    print(str, "can be converted as a palindrome")
    
else:
    print(str, "can not be converted as a palindrome")