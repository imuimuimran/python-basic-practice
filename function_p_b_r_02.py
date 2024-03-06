# passed by refference
def modify_list(list1):
    print("The inside function list is:", list1)
    list1.remove(3)
    print("The inside function list is:", list1)
    list1.pop()
    print("The inside function list is:", list1)
    list2 = [5, 6]
    list1.extend(list2)
    print("The inside function list is:", list1)
    
list1 = [1, 2, 3, 4]
print("The outside of the list before using function is:", list1)
modify_list(list1)
print("The outside of the list is:", list1)