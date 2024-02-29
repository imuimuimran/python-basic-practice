# Check if a number is four digit number or not?
number = int(input("Enter a four digit number:"))

if number >= 1000 and number <= 9999:
    print(number, "is a four digit number")
else:
    print(number, "is not a four digit number")