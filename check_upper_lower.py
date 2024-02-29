letter = input("Enter a letter: ")

if letter.islower():
    print(letter, "is lower case")
elif letter.isupper():
    print(letter, "is upper case")
else:
    print("The input is not a letter")