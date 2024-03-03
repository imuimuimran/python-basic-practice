for i in range(20, 23):
    print("Roll No: ", i)
    for j in range(3):
        if j == 0:
            number = int(input("Bangla: "))
            if number >= 80:
                print("A")
            else:
                print("B")
        elif j == 1:
            number = int(input("English: "))
            if number >= 80:
                print("A")
            else:
                print("B")
        else:
            number = int(input("Math: "))
            if number >= 80:
                print("A")
            else:
                print("B")