total_extended_price = 0
order_count = 0

file = open("M7P4.txt", "r")

item = file.readline().strip()

while item != "":
    quantity = int(file.readline())
    price = float(file.readline())

    extended_price = quantity * price
    total_extended_price = total_extended_price + extended_price
    order_count = order_count + 1

    print("Item:", item)
    print("Quantity:", quantity)
    print("Price: $", format(price, ",.2f"))
    print("Extended Price: $", format(extended_price, ",.2f"))
    print()

    item = file.readline().strip()

file.close()

average_order = total_extended_price / order_count

print ("Total Extended Price: $", format(total_extended_price, ",.2f"))
print ("Number of Orders:", order_count)
print ("Average Order: $", format(average_order, ",.2f"))