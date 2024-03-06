# passed by refference
def modify_list(list1):
    list1.append(5)
    print("The inside function list is:", list1)
    
list1 = [1, 2, 3, 4]
modify_list(list1)
print("The outside of the list is:", list1)