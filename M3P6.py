purchase_price = float(input("Enter the purchase price per share: "))
current_price = float(input("Enter the current stock price: "))
quantity = float(input("Enter the quantity of stock: "))

value_change = (current_price - purchase_price) * quantity

print(f"The value change of the stock is: ${value_change:.2f}")