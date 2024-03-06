def print_Student_info(**kwargs):
    for x,y in kwargs.items():
        print(x, "is", y)
     
# Keyword arguments   
print("Student 1 information is: ")
print_Student_info(name = 'Tahsan Akram', Age = 16, result = 5.0)

print("Student 2 information is: ")
print_Student_info(name = 'Ruzina Sabera', Age = 14, result = 5.0)