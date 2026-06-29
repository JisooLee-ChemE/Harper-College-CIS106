quantity = float(input("Enter the quantity: "))

if quantity >= 10000:
    price = 10
elif quantity >= 5000 and quantity < 10000:
    price = 20
else:
    price = 30

extended_price = quantity * price
tax = extended_price * 0.07
total_price = extended_price + tax

print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax Amount: ${tax:.2f}")
print(f"Total Price: ${total_price:.2f}")