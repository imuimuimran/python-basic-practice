def outer_function():
    print("This is first function")
    def inner_function():
        print("This is inner function")
        
    print("This is outer first function")
    inner_function()
    print("This is outer function")
    
outer_function()