for i in range(20, 23):
    print("Obtained score", i)
    for j in range(3):
        if j == 0:
            number = int(input("Bangla: "))
            if number >=80:
                print("A+")
            else:
                print("Fail")
        elif j == 1:
            number = int(input("English: "))
            if number >=80:
                print("A+")
            else:
                print("Fail")
        else:
            number = int(input("Math: "))
            if number >=80:
                print("A+")
            else:
                print("Fail")
            