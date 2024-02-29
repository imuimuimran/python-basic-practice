# Check if a number is divisible by 3 and 5 but not divisible by 15
num = int(input("Enter a number: "))

if num % 15 == 0 :
    print(num, "is divisible by 15")
else:
    if num % 3 == 0 or num % 5 == 0:
        print(num, "is not divisible by 15 but divisible by 3 and 5")
    else:
        print(num, "is not divisible by 3, 5")
        