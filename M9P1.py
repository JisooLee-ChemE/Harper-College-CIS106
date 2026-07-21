def compiute_total(quantity, unitprice):
    total = quantity * unitprice
    
    if total > 100000.00:
        total = total * 0.90

    return total

total_extended_price = 0.0

response = input("Do you want to enter item information? Enter Yes to continue: ")

while response == "Yes" or response == "yes" or response == "Y" or response == "y":
    quantity = float(input("Enter the quantity of the item: "))
    unit_price = float(input("Enter the unit price of the item: "))

    extended_price = compiute_total(quantity, unit_price)

    total_extended_price = total_extended_price + extended_price

    print("Quantity:", quantity)
    print("Unit Price:", format(unit_price, ".2f"))
    print("Extended Price:", format(extended_price, ".2f"))
    print()

    response = input("Do you want to enter item information? Enter Yes to continue: ")

print("Total Extended Price: $", format(total_extended_price, ".2f"))