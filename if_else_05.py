math_marks = int(input("Enter math marks: "))
english_marks = int(input("Enter English marks: "))

if math_marks >= 80 and english_marks >= 80:
    print("A grade")
elif math_marks >= 80 or english_marks >= 80:
    print("B grade")
else:
    print("C grade")