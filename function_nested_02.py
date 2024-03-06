def outer_function():
    print("This is first function")
    def inner_function():
        inner_result = "This is inner function"
        return inner_result
    result = inner_function() + " This is outer function"
    return result
    
ans = outer_function()
print(ans)