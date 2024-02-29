# Find the greatest number amonge three using nested loop
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 > num2:
    if num1 > num3:
        print(num1, "is the greatest number")
    else:
        print(num3, "is the greatest number")
else:
    if num2 > num3:
        print(num2, "is the greatest number")
    else:
        print(num3, "is the greatest number")

