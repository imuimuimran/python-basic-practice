cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit gained:", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Total loss:", loss)
else:
    print("There is neither profit nor loss.") 
