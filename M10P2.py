def compute_out_the_door_price(msrp, make, model, electric_code):
    if electric_code == "Y" or electric_code == "y":
        percent_off = 0.30
    elif make == "Honda" and model == "Accord":
        percent_off = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent_off = 0.15
    else:
        percent_off = 0.05

    discount_amount = msrp * percent_off
    new_msrp = msrp - discount_amount
    sales_tax = new_msrp * 0.07
    out_the_door_price = new_msrp + sales_tax

    return out_the_door_price

total_msrp = 0.0
total_sales_price = 0.0

response = input("Do you want to enter vehicle information? Enter Yes to continue: ")   

while response == "Yes" or response == "yes" or response == "Y" or response == "y":
    make = input("Enter car make: ")
    model = input("Enter car model: ")
    electric_code = input("Is the car electric? Enter Y for Yes or N for No: ")
    msrp = float(input("Enter the MSRP: "))

    out_the_door_price = compute_out_the_door_price(msrp, make, model, electric_code)

    total_msrp = total_msrp + msrp
    total_sales_price = total_sales_price + out_the_door_price

    print("Make:", make)
    print("Model:", model)
    print("Electric Code:", electric_code)
    print("MSRP: $", format(msrp, ".2f"))
    print("Out the Door Price: $", format(out_the_door_price, ".2f"))
    print()

    response = input("Do you want to enter vehicle information? Enter Yes to continue: ")

print("Total MSRP: $", format(total_msrp, ".2f"))
print("Total Sales Price: $", format(total_sales_price, ".2f"))