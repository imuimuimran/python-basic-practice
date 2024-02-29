marks = int(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    print("You got A")
elif marks >= 60 and marks <= 79:
    print("You got B")
elif marks >= 40 and marks <= 59:
    print("You got C")
elif marks >= 0 and marks <= 39:
    print("Fail!")
else:
    print("Invalid number!")