def update_student_info(student, new_info):
    student.update(new_info)
    return student

student1 = {}

num_pair = int(input("Enter how the number of key-value pairs: "))

for _ in range(num_pair):
    key = input("Enter Key: ")
    value = input("Enter value: ")
    student1[key] = value


print("initial student information: ")
print(student1)

new_student = {}

num_pair2 = int(input("Enter how the number of key-value pairs: "))

for _ in range(num_pair2):
    key = input("Enter Key: ")
    value = input("Enter value: ")
    new_student[key] = value


updated_information = update_student_info(student1, new_student)

print("updated information of student: ")
print(updated_information)