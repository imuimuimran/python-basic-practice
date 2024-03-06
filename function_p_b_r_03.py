# passed by refference
def modify_list(list1):
    print("The inside function list is:", list1)
    # it will not work, because here is created a new list with assign operator, which is not affected in the function
    list = [3, 4, 5, 6]
    print("The inside function list is:", list1)
    
list1 = [1, 2, 3, 4]
print("The outside of the list before using function is:", list1)
modify_list(list1)
print("The outside of the list is:", list1)