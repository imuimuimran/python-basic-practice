def update_student_info(student, new_info):
    student.update(new_info)
    return student

student1 = {
    'Name' : 'Fahim',
    'Roll' : 1,
    'Class' : 'IX'
}

print("initial student information: ")
print(student1)

new_student = {
    'Name' : 'Irisha',
    'Roll' : 2,
    'Class' : 'XI'
}

updated_information = update_student_info(student1, new_student)

print("updated information of student: ")
print(updated_information)