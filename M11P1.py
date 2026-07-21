def compute_discount(quantity, price, discount_rate):
    extended_price = quantity * price
    discount_amount = extended_price * discount_rate
    discounted_price = extended_price - discount_amount

    return discounted_price, discount_amount

quantity = float(input("Enter the quantity of the item: "))
price = float(input("Enter the unit price of the item: "))
discount_rate = float(input("Enter the discount rate (as a decimal): "))

discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

print("Quantity:", quantity)
print("Price: $", format(price, ".2f"))
print("Discount Amount: $", format(discount_amount, ".2f"))
print("Discounted Price: $", format(discounted_price, ".2f"))