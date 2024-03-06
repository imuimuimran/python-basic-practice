def outer_function():
    x = 1
    
    def inner_function():
        y = 2
        result = x + y
        return result
    return inner_function()


ans = outer_function()
print(ans)