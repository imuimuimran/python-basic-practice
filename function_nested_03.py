def outer_function(str, str2):
    print("This is first function")
    def inner_function():
        inner_result = "This is inner function"
        return inner_result
    result = str + inner_function() + str2 + " This is outer function"
    return result

str = "Hi, "    
str2 = " and"
ans = outer_function(str, str2)
print(ans)