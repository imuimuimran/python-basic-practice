num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator: ")

match operator:
    case "+":
        print("The sum of ", num1, "+", num2, "is:", num1 + num2)
    case "-":
        print("The difference of ", num1, "-", num2, "is:", num1 - num2)
    case "*":
        print("The multiplication of ", num1, "*", num2, "is:", num1 * num2)
    case "/":
        print("The division of ", num1, "/", num2, "is:", num1 / num2)
    case _ :
        print("Enter a valid number.")